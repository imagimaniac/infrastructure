#!/usr/bin/env python3
"""Generate synthetic Pune-like network, routes, TLS and SUMO config."""
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CFG = BASE / "config"


def ensure_dirs():
    CFG.mkdir(parents=True, exist_ok=True)
    (BASE / "data").mkdir(parents=True, exist_ok=True)
    (BASE / "outputs" / "figures").mkdir(parents=True, exist_ok=True)
    (BASE / "outputs" / "reports").mkdir(parents=True, exist_ok=True)


def write_network():
    net_xml = """<?xml version="1.0" encoding="UTF-8"?>
<net version="1.20" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/net_file.xsd">
    <location netOffset="0.00,0.00" convBoundary="0.00,-400.00,800.00,400.00" origBoundary="0.00,-400.00,800.00,400.00" projParameter="!"/>

    <nodes>
        <node id="A1" x="0.00" y="400.00" type="traffic_light"/>
        <node id="A2" x="0.00" y="0.00" type="traffic_light"/>
        <node id="A3" x="0.00" y="-400.00" type="traffic_light"/>
        <node id="B1" x="400.00" y="400.00" type="traffic_light"/>
        <node id="B2" x="400.00" y="0.00" type="traffic_light"/>
        <node id="B3" x="400.00" y="-400.00" type="traffic_light"/>
        <node id="C1" x="800.00" y="400.00" type="traffic_light"/>
        <node id="C2" x="800.00" y="0.00" type="traffic_light"/>
        <node id="C3" x="800.00" y="-400.00" type="traffic_light"/>
    </nodes>

    <edges>
        <edge id="A1_B1" from="A1" to="B1" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B1_A1" from="B1" to="A1" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B1_C1" from="B1" to="C1" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="C1_B1" from="C1" to="B1" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="A2_B2" from="A2" to="B2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B2_A2" from="B2" to="A2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B2_C2" from="B2" to="C2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="C2_B2" from="C2" to="B2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="A3_B3" from="A3" to="B3" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B3_A3" from="B3" to="A3" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B3_C3" from="B3" to="C3" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="C3_B3" from="C3" to="B3" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="A1_A2" from="A1" to="A2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="A2_A1" from="A2" to="A1" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="A2_A3" from="A2" to="A3" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="A3_A2" from="A3" to="A2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B1_B2" from="B1" to="B2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B2_B1" from="B2" to="B1" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B2_B3" from="B2" to="B3" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="B3_B2" from="B3" to="B2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="C1_C2" from="C1" to="C2" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="C2_C1" from="C2" to="C1" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="C2_C3" from="C2" to="C3" priority="-1" numLanes="2" speed="13.89"/>
        <edge id="C3_C2" from="C3" to="C2" priority="-1" numLanes="2" speed="13.89"/>
    </edges>
</net>
"""
    (CFG / "network.net.xml").write_text(net_xml, encoding="utf-8")


def write_routes(seed=42):
    routes = """<?xml version="1.0" encoding="UTF-8"?>
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <vType id="passenger" accel="1.0" decel="4.5" sigma="0.5" length="5" maxSpeed="13.89"/>
    <route id="r1" edges="A1_B1 B1_B2 B2_B3 B3_C3"/>
    <route id="r2" edges="A2_B2 B2_B1 B1_C1"/>
    <route id="r3" edges="C2_B2 B2_A2 A2_A1"/>
    <route id="r4" edges="B1_B2 B2_C2 C2_C3"/>
    <flow id="f1" type="passenger" route="r1" begin="0" end="3600" vehsPerHour="700"/>
    <flow id="f2" type="passenger" route="r2" begin="0" end="3600" vehsPerHour="600"/>
    <flow id="f3" type="passenger" route="r3" begin="0" end="3600" vehsPerHour="600"/>
    <flow id="f4" type="passenger" route="r4" begin="0" end="3600" vehsPerHour="700"/>
</routes>
"""
    (CFG / "routes.rou.xml").write_text(routes, encoding="utf-8")


def write_tls():
    tls = """<?xml version="1.0" encoding="UTF-8"?>
<additional xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/additional_file.xsd">
    <tlLogic id="B1" type="static" programID="fixed" offset="0">
        <phase duration="31" state="GGrrGGrr"/>
        <phase duration="3" state="yyrryyrr"/>
        <phase duration="31" state="rrGGrrGG"/>
        <phase duration="3" state="rryyrryy"/>
    </tlLogic>
    <tlLogic id="B2" type="static" programID="fixed" offset="5">
        <phase duration="31" state="GGrrGGrr"/>
        <phase duration="3" state="yyrryyrr"/>
        <phase duration="31" state="rrGGrrGG"/>
        <phase duration="3" state="rryyrryy"/>
    </tlLogic>
    <tlLogic id="B3" type="static" programID="fixed" offset="10">
        <phase duration="31" state="GGrrGGrr"/>
        <phase duration="3" state="yyrryyrr"/>
        <phase duration="31" state="rrGGrrGG"/>
        <phase duration="3" state="rryyrryy"/>
    </tlLogic>
    <tlLogic id="A2" type="static" programID="fixed" offset="0">
        <phase duration="31" state="GrrG"/>
        <phase duration="3" state="yrry"/>
        <phase duration="31" state="rGGr"/>
        <phase duration="3" state="ryyr"/>
    </tlLogic>
    <tlLogic id="C2" type="static" programID="fixed" offset="2">
        <phase duration="31" state="GrrG"/>
        <phase duration="3" state="yrry"/>
        <phase duration="31" state="rGGr"/>
        <phase duration="3" state="ryyr"/>
    </tlLogic>
</additional>
"""
    (CFG / "tls.add.xml").write_text(tls, encoding="utf-8")


def write_sumocfg():
    sumocfg = """<?xml version="1.0" encoding="UTF-8"?>
<configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/sumoConfiguration.xsd">
    <input>
        <net-file value="network.net.xml"/>
        <route-files value="routes.rou.xml"/>
        <additional-files value="tls.add.xml"/>
    </input>
    <time>
        <begin value="0"/>
        <end value="3600"/>
    </time>
    <output>
        <tripinfo-output value="../data/tripinfo.xml"/>
        <summary-output value="../data/summary.xml"/>
    </output>
    <processing>
        <time-to-teleport value="-1"/>
    </processing>
    <report>
        <duration-log.statistics value="true"/>
    </report>
</configuration>
"""
    (CFG / "simulation.sumocfg").write_text(sumocfg, encoding="utf-8")


def main():
    ensure_dirs()
    write_network()
    write_routes()
    write_tls()
    write_sumocfg()
    print(f"Generated synthetic configs in {CFG}")


if __name__ == "__main__":
    main()
