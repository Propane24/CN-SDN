from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    if not packet.parsed:
        log.warning("Ignoring incomplete packet")
        return

    ip_packet = packet.find('ipv4')

    # If not IP packet → flood normally
    if not ip_packet:
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)
        return

    src = ip_packet.srcip
    dst = ip_packet.dstip

    # 🚫 FIREWALL RULE (BLOCK)
    if str(src) == "10.0.0.1" and str(dst) == "10.0.0.3":
        log.info("BLOCKED: %s -> %s", src, dst)

        # Install drop rule (so future packets auto-drop)
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match(dl_type=0x0800, nw_src=src, nw_dst=dst)
        msg.actions = []  # no action = drop
        event.connection.send(msg)
        return

    # ✅ ALLOW TRAFFIC (forward/flood)
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("🔥 SDN Firewall Controller Started (POX)")
