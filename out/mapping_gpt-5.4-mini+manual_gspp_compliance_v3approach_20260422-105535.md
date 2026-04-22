# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:55:35

**Gesamt:** 10 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 1 |
| Teilweise abgedeckt | 9 |
| Keine Abdeckung | 0 |

## Voll abgedeckt (1)

### ARCH.5.1.8 — Inspektion verschlüsselter Verbindungen
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A21` [Standard] Temporäre Entschlüsselung des Datenverkehrs — _NET.3.2 Firewall_
  - `NET.3.2.A28` [Hoch] Zentrale Filterung von aktiven Inhalten — _NET.3.2 Firewall_
  - `NET.1.1.A12` [Basis] Absicherung ausgehender interner Kommunikation zum Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A20` [Standard] Absicherung von grundlegenden Internetprotokollen — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A21=0.47, NET.3.2.A28=0.47, NET.1.1.A12=0.34, NET.3.2.A20=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9400 gs_ids=NET.3.2.A28;NET.3.2.A21
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6855 gs_ids=NET.3.2.A20;NET.1.1.A12
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A28 deckt die zentrale Filterung aktiver Inhalte ab und nennt ausdrücklich die Entschlüsselung verschlüsselten Datenverkehrs durch Sicherheitsproxies. NET.3.2.A21 ergänzt dies um die temporäre Entschlüsselung verschlüsselter Verbindungen in nicht vertrauenswürdige Netze, um das Protokoll zu verifizieren und Daten auf Schadsoftware zu prüfen. Zusammen bilden beide Anforderungen den Kern der GS++-Anforderung "Inspektion verschlüsselter Verbindungen" ab: verschlüsselten Traffic entschlüsseln, über Proxy/Sicherheitsproxy inspizieren und Inhalte anhand der Sicherheitsziele filtern.
- **Lücken:** [gpt-5.4-mini] Keine wesentlichen Lücken; die GS++-Beispiele zu HTTPS/TLS-Proxy-Inspektion werden inhaltlich durch die beiden Firewall-Anforderungen abgedeckt. Details zu Endstellen-Inspektion oder konkreten Produktbeispielen sind in den Kandidaten nicht ausgeführt, aber für die fachliche Abdeckung nicht erforderlich.

## Teilweise abgedeckt (9)

### ARCH.1.1.1 — Dokumentation
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `APP.2.1.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für Verzeichnisdienste — _APP.2.1 Allgemeiner Verzeichnisdienst_
  - `APP.6.A10` [Standard] Erstellung einer Sicherheitsrichtlinie für den Einsatz der Software — _APP.6 Allgemeine Software_
  - `APP.7.A6` [Standard] Dokumentation der Anforderungen an die Individualsoftware — _APP.7 Entwicklung von Individualsoftware_
  - `CON.10.A11` [Standard] Softwarearchitektur einer Webanwendung — _CON.10 Entwicklung von Webanwendungen_
  - `CON.8.A12` [Standard] Ausführliche Dokumentation — _CON.8 Software-Entwicklung_
  - `DER.3.1.A6` [Standard] Definition der Prüfungsgrundlage und eines einheitlichen Bewertungsschemas — _DER.3.1 Audits und Revisionen_
  - `DER.4.A12` [Hoch] Dokumentation im Notfallmanagement-Prozess — _DER.4 Notfallmanagement_
  - `IND.1.A11` [Standard] Sichere Beschaffung und Systementwicklung — _IND.1 Prozessleit- und Automatisierungstechnik_
  - `NET.1.2.A12` [Standard] Ist-Aufnahme und Dokumentation des Netzmanagements — _NET.1.2 Netzmanagement_
  - `SYS.1.1.A11` [Standard] Festlegung einer Sicherheitsrichtlinie für Server — _SYS.1.1 Allgemeiner Server_
  - `SYS.4.4.A6` [Standard] Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.2.1.A1=0.45, APP.6.A10=0.45, APP.7.A6=0.45, CON.10.A11=0.45, CON.8.A12=0.45, DER.3.1.A6=0.45, DER.4.A12=0.45, IND.1.A11=0.45, NET.1.2.A12=0.45, SYS.1.1.A11=0.45, SYS.4.4.A6=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=APP.6.A10;APP.2.1.A1;CON.8.A12;DER.4.A12;NET.1.2.A12;IND.1.A11;CON.10.A11;APP.7.A6;DER.3.1.A6;SYS.1.1.A11;SYS.4.4.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Kandidaten decken den Kernaspekt „Dokumentation von Verfahren und Regelungen“ in mehreren fachlichen Ausprägungen ab: APP.6.A10 verlangt die Zusammenfassung von Einsatz- und Betriebsregeln in einer Sicherheitsrichtlinie; APP.2.1.A1 fordert eine Sicherheitsrichtlinie für den Verzeichnisdienst; CON.8.A12, CON.10.A11 und APP.7.A6 behandeln die Dokumentation von Entwicklungs-/Architektur- und Anforderungsinhalten; NET.1.2.A12, IND.1.A11, DER.4.A12, DER.3.1.A6, SYS.1.1.A11 und SYS.4.4.A6 verlangen die Dokumentation von Zuständen, Verfahren, Richtlinien oder Prüfschemata in konkreten Domänen. Damit wird die generelle Pflicht zur Dokumentation organisatorischer Regeln inhaltlich klar berührt. Allerdings adressiert keine der Anforderungen die GS++-Aussage in der Breite als allgemeine Dokumentationspflicht für Verfahren und Regelungen der Architektur ohne Domänenbindung; die Kandidaten sind überwiegend domänenspezifisch oder betreffen andere Regelungsarten (z. B. Auditbewertung, Entwicklungsdokumentation, Richtlinien für einzelne Technologien).
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine, domänenübergreifende Dokumentation aller Architektur-Verfahren und -Regelungen sowie die explizite Zielsetzung der Verbindlichkeit/Wiederholbarkeit als allgemeine organisatorische Anforderung. Mehrere Kandidaten sind auf spezifische Teilbereiche begrenzt (Software, Netz, Server, IoT, Audit, Notfallmanagement) und ersetzen keine generische Architektur-Dokumentation.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.79
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A11` [Basis] Absicherung eingehender Kommunikation vom Internet in das interne Netz — _NET.1.1 Netzarchitektur und -design_
  - `CON.7.A7` [Basis] Sicherer Remote-Zugriff auf das Netz der Institution — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `CON.7.A8` [Basis] Sichere Nutzung von öffentlichen WLANs — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `INF.10.A6` [Standard] Einrichtung sicherer Netzzugänge — _INF.10 Besprechungs-, Veranstaltungs- und Schulungsräume_
  - `NET.1.1.A10` [Basis] DMZ-Segmentierung für Zugriffe aus dem Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A18` [Standard] P-A-P-Struktur für die Internet-Anbindung — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A9` [Basis] Grundlegende Absicherung der Kommunikation mit nicht vertrauenswürdigen Netzen — _NET.1.1 Netzarchitektur und -design_
  - `NET.2.1.A15` [Hoch] Verwendung eines VPN zur Absicherung von WLANs — _NET.2.1 WLAN-Betrieb_
  - `SYS.3.1.A8` [Standard] Sicherer Anschluss von Laptops an Datennetze — _SYS.3.1 Laptops_
  - `SYS.3.2.1.A28` [Standard] Verwendung der Filteroption für Webseiten — _SYS.3.2.1 Allgemeine Smartphones und Tablets_
  - `NET.3.3.A11` [Standard] Sichere Anbindung eines externen Netzes — _NET.3.3 VPN_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A11=0.79, CON.7.A7=0.43, CON.7.A8=0.43, INF.10.A6=0.43, NET.1.1.A10=0.43, NET.1.1.A18=0.43, NET.1.1.A4=0.43, NET.1.1.A9=0.43, NET.2.1.A15=0.43, SYS.3.1.A8=0.43, SYS.3.2.1.A28=0.43, NET.3.3.A11=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=NET.1.1.A4;NET.1.1.A9;NET.1.1.A10;NET.1.1.A11;NET.1.1.A18;CON.7.A7;CON.7.A8;NET.2.1.A15;SYS.3.1.A8;SYS.3.2.1.A28;INF.10.A6
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] Die Anforderungen NET.1.1.A4, NET.1.1.A9, NET.1.1.A10, NET.1.1.A11 und NET.1.1.A18 decken Teile des Themas Netzdesign und externe Netzanbindungen ab: Sie regeln Zonentrennung, DMZ, sichere Kommunikationskanäle, VPN-Zugriffe und P-A-P-Strukturen, also technische Schutzmaßnahmen an Internet- und externen Netzanschlüssen. CON.7.A7, CON.7.A8, NET.2.1.A15, SYS.3.1.A8 und SYS.3.2.1.A28 behandeln sichere mobile bzw. WLAN-basierte Zugänge, bei denen eine VPN-Nutzung bzw. die Absicherung direkter Internetzugänge relevant ist. INF.10.A6 adressiert ebenfalls die Verhinderung unerwünschter gleichzeitiger Verbindungen von internem Netz und Internet in Räumen mit externen Anschlüssen. Insgesamt wird damit das Ziel der Einschränkung von Verbindungen über externe Netzanschlüsse in mehreren Szenarien abgedeckt, jedoch nicht vollständig auf architektonischer Ebene für alle externen Netzanschlüsse im Sinne einer generellen Netzentwurfsregel.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die generelle, übergreifende Architekturvorgabe, externe Netzanschlüsse als solche flächendeckend zu beschränken. Die Kandidaten regeln vor allem konkrete Ausprägungen (Internet-/DMZ-Anbindung, VPN, WLAN, mobile Endgeräte, Besprechungsräume), aber keine einheitliche, allgemeine Designregel für alle externen Anschlussarten und alle Segmentgrenzen. Zudem ist die GS++-Formulierung eher als globale Architekturleitlinie formuliert, während mehrere Kandidaten nur Spezialfälle oder Einzelmaßnahmen adressieren.

### ARCH.2.2.11 — Physische Segmentierung
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `INF.14.A28` [Hoch] Physische Trennung der GA — _INF.14 Gebäudeautomation_
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A32` [Hoch] Physische Trennung von Management-Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.2.A32` [Hoch] Physische Trennung des Managementnetzes — _NET.1.2 Netzmanagement_
  - `NET.1.2.A33` [Hoch] Physische Trennung von Management-Segmenten — _NET.1.2 Netzmanagement_
  - `SYS.1.5.A15` [Standard] Betrieb von Gast-Betriebssystemen mit unterschiedlichem Schutzbedarf — _SYS.1.5 Virtualisierung_
  - `SYS.1.5.A4` [Basis] Sichere Konfiguration eines Netzes für virtuelle Infrastrukturen — _SYS.1.5 Virtualisierung_
  - `SYS.1.8.A15` [Standard] Sichere Trennung von Mandanten in Speicherlösungen — _SYS.1.8 Speicherlösungen_
  - `SYS.2.5.A2` [Basis] Planung der verwendeten Netze für virtuelle Clients — _SYS.2.5 Client-Virtualisierung_
  - `NET.1.1.A22` [Standard] Spezifikation des Segmentierungskonzepts — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A23` [Standard] Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A31` [Hoch] Physische Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A33` [Hoch] Mikrosegmentierung des Netzes — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A28=0.45, INF.14.A6=0.45, NET.1.1.A32=0.45, NET.1.1.A4=0.45, NET.1.2.A32=0.45, NET.1.2.A33=0.45, SYS.1.5.A15=0.45, SYS.1.5.A4=0.45, SYS.1.8.A15=0.45, SYS.2.5.A2=0.45, NET.1.1.A22=0.34, NET.1.1.A23=0.34, NET.1.1.A31=0.34, NET.1.1.A33=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=INF.14.A28;NET.1.1.A4;NET.1.2.A32;NET.1.1.A32;NET.1.2.A33;SYS.2.5.A2;SYS.1.5.A4;SYS.1.5.A15;INF.14.A6;SYS.1.8.A15
[manual:gspp_compliance_v3approach] coverage=teilweise confidence=0.6711 gs_ids=NET.1.1.A31;NET.1.1.A23;NET.1.1.A33;NET.1.1.A22
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.11 fordert, Netzsegmente nach Möglichkeit physisch zu trennen, um Umgehungen der Netztrennung durch virtuelle Vernetzung zu erschweren. Inhaltlich passen dazu insbesondere NET.1.1.A4 (physische Trennung von internen Netz, DMZ und Außenanbindungen), NET.1.1.A32 und NET.1.2.A32 sowie NET.1.2.A33 (physische Trennung von Management- bzw. Management-Segmenten), INF.14.A28 (physisch getrennte GA-Netze), INF.14.A6 (bei Gebäudenetzen teils logische/teils physische Separierung), SYS.2.5.A2 und SYS.1.5.A4 (Vermeidung von Umgehung der Netztrennung in Virtualisierungsumgebungen), SYS.1.5.A15 (ausreichend sichere Netztrennung bei gemeinsam betriebenen Gast-OS) sowie SYS.1.8.A15 (Netzsegmentierung zur Mandantentrennung in Speicher-/IP-iSCSI-Umgebungen). Diese Anforderungen treffen den Kern 'physische Segmentierung' bzw. 'verhindern von Umgehung über virtuelle Netze' in verschiedenen technischen Domänen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der allgemeine, domänenübergreifende Grundsatz der physischen Segmentierung für beliebige Netzsegmente als Architekturprinzip. Mehrere Kandidaten sind nur auf Spezialfälle begrenzt (Management-Netze, GA, virtuelle Clients, Speicherlösungen) oder verlangen nur 'physische Trennung' unter bestimmten Bedingungen. Eine explizite, generische Architekturforderung, alle relevanten Netzsegmente physisch statt nur logisch zu trennen, ist durch die Kandidaten nur teilweise abgedeckt.

### ARCH.2.2.8 — Segmentierung von Test und Betrieb
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `APP.4.4.A1` [Basis] Planung der Separierung der Anwendungen — _APP.4.4 Kubernetes_
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.4.2.A16` [Hoch] Trennung des Daten- und VoIP-Netzes — _NET.4.2 VoIP_
  - `OPS.1.1.6.A13` [Standard] Trennung der Testumgebung von der Produktivumgebung — _OPS.1.1.6 Software-Tests und -Freigaben_
  - `SYS.1.7.A33` [Hoch] Trennung von Test- und Produktionssystemen unter z/OS — _SYS.1.7 IBM Z_
- **Begründung:** Gemittelte Kandidatenscores: APP.4.4.A1=0.42, INF.14.A6=0.42, NET.4.2.A16=0.42, OPS.1.1.6.A13=0.42, SYS.1.7.A33=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=OPS.1.1.6.A13;APP.4.4.A1;INF.14.A6;NET.4.2.A16;SYS.1.7.A33
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.6.A13 deckt die Trennung der Testumgebung von der Produktivumgebung im Software-Testprozess direkt ab. APP.4.4.A1 behandelt ebenfalls die Separierung von Test- und Produktions-Betriebsumgebungen und nennt ausdrücklich die passende Netz-/Cluster-Architektur. INF.14.A6 und NET.4.2.A16 sind passende Netzsegmentierungs-Anforderungen, da sie die logische Trennung von Netzen und die kontrollierte Kommunikation zwischen Segmenten bzw. zwischen VoIP- und Datennetz regeln; sie stützen damit den Aspekt der Einschränkung von Verbindungen zwischen Umgebungen. SYS.1.7.A33 ist inhaltlich ähnlich, da es die Trennung von Test- und Produktionssystemen unter z/OS fordert. Zusammen adressieren die Kandidaten den Kern der geforderten Segmentierung zwischen Test und Betrieb.
- **Lücken:** [gpt-5.4-mini] Die GS++-Anforderung ist bewusst allgemein für die Netzarchitektur formuliert und spricht explizit von Verbindungen zwischen Testumgebungen und Betrieb. Die Kandidaten decken dies zwar in Teilen ab, aber nicht als einheitliche, generische Architekturvorgabe für alle Umgebungen und Technologien. NET.4.2.A16 ist fachlich auf VoIP beschränkt, SYS.1.7.A33 auf z/OS, und OPS.1.1.6.A13 bzw. APP.4.4.A1 sind stärker auf Software-Test/Container-Umgebungen fokussiert als auf allgemeine Netzwerksegmentierung. Daher keine vollständige Abdeckung.

### ARCH.2.2.9 — Segmentierung von IPv4 und IPv6
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A20` [Standard] Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A17` [Standard] Deaktivierung von IPv4 oder IPv6 — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A20=0.44, NET.3.2.A17=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=NET.1.1.A20;NET.3.2.A17
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.1.1.A20 adressiert die Zuordnung unterschiedlicher IPv4-/IPv6-Endgerätegruppen zu dedizierten Subnetzen und trifft damit den Kern der gewünschten Segmentierung nach Protokoll. NET.3.2.A17 ergänzt dies, indem nicht benötigtes IPv4 oder IPv6 an Firewall-Netzzugangspunkten deaktiviert werden soll; das unterstützt die Einschränkung von Verbindungen zwischen IPv4 und IPv6 ebenfalls technisch. Beide Anforderungen zielen jedoch primär auf Trennung bzw. Abschaltung von Protokollen oder Protokollnutzung, nicht ausdrücklich auf eine allgemeine Architekturvorgabe zur Einschränkung aller Verbindungen zwischen IPv4- und IPv6-Segmenten in jedem Fall.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die explizite Vorgabe, Verbindungen zwischen IPv4- und IPv6-Segmenten generell architektonisch zu beschränken, auch wenn beide Protokolle parallel benötigt werden. Die Kandidaten behandeln vor allem dedizierte Subnetze bzw. Deaktivierung ungenutzter Protokolle, nicht die umfassende Regelung aller Interaktionen zwischen IPv4- und IPv6-Bereichen.

### ARCH.5.1.12 — Software-definierte Verbindungen
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A2` [Basis] Festlegen der Firewall-Regeln — _NET.3.2 Firewall_
  - `OPS.1.2.5.A25` [Standard] Entkopplung der Kommunikation bei der Fernwartung — _OPS.1.2.5 Fernwartung_
  - `SYS.3.1.A3` [Basis] Einsatz von Personal Firewalls — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A2=0.43, OPS.1.2.5.A25=0.43, SYS.3.1.A3=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=NET.3.2.A2;SYS.3.1.A3;OPS.1.2.5.A25
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A2 deckt die grundsätzliche technische Einschränkung von Kommunikationsverbindungen über festgelegte Firewall-Regeln ab. SYS.3.1.A3 ergänzt dies durch die restriktive Filterung auf Endgeräten mittels Personal Firewall. OPS.1.2.5.A25 passt insofern, als über Sprungserver die Kommunikation entkoppelt und nur über vertrauenswürdige Systeme zugelassen wird. Gemeinsam bilden diese Anforderungen jedoch nur statische bzw. regelbasierte Zugriffsbeschränkungen ab; die zentrale GS++-Forderung nach dynamischen Kriterien, also kontextabhängiger Bewertung aktueller Merkmale wie Gerätezustand, Auslastung, Standort oder Risiko, wird nicht beschrieben.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die dynamische Entscheidungslogik und kontextabhängige/policy-basierte Bewertung von Verbindungen (z. B. device posture, aktuelle Auslastung, Standort, Risikobewertung), wie sie für software-definierte Verbindungen wesentlich ist. Die Kandidaten behandeln nur statische Allowlist-/Filter- oder Segmentierungsmechanismen.

### ASST.2.1.1 — Informationsverantwortung
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `ORP.1.A2` [Basis] Zuweisung der Zuständigkeiten — _ORP.1 Organisation_
- **Begründung:** Gemittelte Kandidatenscores: ORP.1.A2=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9700 gs_ids=ORP.1.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.1.A2 deckt die zentrale Kernforderung ab, für alle Geschäftsprozesse, Anwendungen, IT-Systeme und Kommunikationsverbindungen festzulegen, wer zuständig ist, und diese Zuständigkeiten den Mitarbeitenden bekannt zu machen. Das entspricht inhaltlich der GS++-Anforderung ASST.2.1.1 zur Zuweisung der Zuständigkeit für die Verarbeitung von Informationen und Assets bzw. zum Asset Ownership. Die geforderte klare Zuständigkeit für Informationen kann über die Zuordnung zu Prozessen, Anwendungen und Systemen umgesetzt werden, wie auch in der GS++-Guidance beschrieben.
- **Lücken:** [gpt-5.4-mini] Die GS-Anforderung nennt Informationen und Assets nicht explizit als eigenständige Inventarobjekte, sondern ordnet Zuständigkeiten über Prozesse, Anwendungen, IT-Systeme und Verbindungen zu. Inhaltlich ist der Verantwortungsaspekt jedoch voll getroffen.

### ASST.2.2.1 — Aufdecken unautorisierter IT-Systeme
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.1.A6` [Standard] Durchführung des IT-Asset-Managements — _OPS.1.1.1 Allgemeiner IT-Betrieb_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.1.A6=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9600 gs_ids=OPS.1.1.1.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.1.A6 passt inhaltlich am besten, weil es die Erstellung, regelmäßige Prüfung und Pflege einer vollständigen Übersicht aller vorhandenen IT-Assets fordert. Damit wird das Inventarisieren und das Erkennen nicht erfasster bzw. unbekannter Systeme organisatorisch unterstützt. Die GS++-Anforderung ASST.2.2.1 verlangt jedoch speziell das aktive Aufdecken unautorisierter IT-Systeme im Netz, z. B. mittels Netzscans, passiver Analyse oder WLAN-Erkennung, sowie die anschließende Behandlung der Funde. Diese detektivisch-technischen Aspekte werden von OPS.1.1.1.A6 nicht vollständig abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkreten Maßnahmen zum Aufdecken unautorisierter Systeme (aktive/passive Netzüberwachung, WLAN-Detektion) sowie die Behandlung gefundener Systeme wie Quarantäne, Entfernung oder nachträgliche Autorisierung.

### ASST.7.1 — Nicht mehr benötigte Anwendungen
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `APP.6.A13` [Standard] Deinstallation von Software — _APP.6 Allgemeine Software_
  - `SYS.1.9.A15` [Standard] Härtung des Terminalservers — _SYS.1.9 Terminalserver_
  - `SYS.2.1.A16` [Standard] Deaktivierung und Deinstallation nicht benötigter Komponenten und Kennungen — _SYS.2.1 Allgemeiner Client_
  - `SYS.3.2.2.A7` [Standard] Installation von Apps — _SYS.3.2.2 Mobile Device Management (MDM)_
  - `SYS.4.4.A13` [Standard] Deaktivierung und Deinstallation nicht benötigter Komponenten — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.6.A13=0.43, SYS.1.9.A15=0.43, SYS.2.1.A16=0.43, SYS.3.2.2.A7=0.43, SYS.4.4.A13=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8700 gs_ids=APP.6.A13;SYS.2.1.A16;SYS.1.9.A15;SYS.3.2.2.A7;SYS.4.4.A13
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] APP.6.A13 passt inhaltlich am direktesten, weil es die Deinstallation von Software und das Entfernen nicht mehr benötigter Dateien/Einträge regelt. SYS.2.1.A16 ergänzt dies für Clients um die Deinstallation nicht benötigter Programme, Dienste und Kennungen, SYS.1.9.A15 für Terminalserver und SYS.4.4.A13 für IoT-Geräte mit nicht benötigten Anwendungen/Diensten. SYS.3.2.2.A7 adressiert zusätzlich die verwaltete Deinstallation von Apps per MDM. Zusammen decken diese Anforderungen den Kern der geforderten Deinstallation nicht mehr benötigter Anwendungsinstanzen ab, aber nicht vollständig die GS++-Spezifika wie die explizite Behandlung von Cloud-Instanzen außerhalb der Kontrolle der Institution, das vollständige Entfernen aller zugehörigen Konfigurationen/Zugriffsrechte als geregelter Prozess über alle Umgebungen hinweg sowie die allgemeine, bausteinübergreifende Anforderung für alle Anwendungstypen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind insbesondere: geregelte Löschung aller zugehörigen Konfigurationen und Berechtigungen, explizite Berücksichtigung von Cloud-Anwendungsinstanzen ohne eigene Kontrolle inklusive Löschung der Daten in der Cloud, sowie eine allgemeingültige Vorgabe für sämtliche Plattformen und Anwendungstypen jenseits der spezifischen Domänen Client/Terminalserver/IoT/MDM/Allgemeine Software.
