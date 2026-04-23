# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:54:08

**Gesamt:** 20 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 18 |
| Keine Abdeckung | 2 |

## Teilweise abgedeckt (18)

### ARCH.1.1.1 — Dokumentation
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `APP.2.1.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für Verzeichnisdienste — _APP.2.1 Allgemeiner Verzeichnisdienst_
  - `APP.6.A10` [Standard] Erstellung einer Sicherheitsrichtlinie für den Einsatz der Software — _APP.6 Allgemeine Software_
  - `DER.4.A12` [Hoch] Dokumentation im Notfallmanagement-Prozess — _DER.4 Notfallmanagement_
  - `SYS.1.1.A11` [Standard] Festlegung einer Sicherheitsrichtlinie für Server — _SYS.1.1 Allgemeiner Server_
  - `SYS.4.4.A6` [Standard] Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.2.1.A1=0.45, APP.6.A10=0.45, DER.4.A12=0.45, SYS.1.1.A11=0.45, SYS.4.4.A6=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=APP.6.A10;DER.4.A12;APP.2.1.A1;SYS.1.1.A11;SYS.4.4.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Kandidaten APP.6.A10, DER.4.A12, APP.2.1.A1, SYS.1.1.A11 und SYS.4.4.A6 decken jeweils die Forderung ab, Regeln bzw. Richtlinien zu dokumentieren und diese aktuell bzw. nachvollziehbar zu halten. APP.6.A10 verlangt, Regelungen für Einsatz und Betrieb in einer Sicherheitsrichtlinie zusammenzufassen; SYS.1.1.A11 und SYS.4.4.A6 verlangen die Konkretisierung und Dokumentation von Anforderungen in Sicherheitsrichtlinien; APP.2.1.A1 fordert eine Sicherheitsrichtlinie für Verzeichnisdienste; DER.4.A12 fordert die Dokumentation von Abläufen, Arbeitsergebnissen und Entscheidungen. Damit ist der allgemeine Dokumentationsgedanke der GS++-Anforderung inhaltlich gut getroffen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der spezifische Anspruch, dass die Architektur selbst die Verfahren und Regelungen dokumentieren muss, also die Zuordnung der Dokumentation zur Architektur- bzw. Managementebene. Ebenfalls fehlt die explizite Zielgruppenorientierung der Dokumentation sowie der Hinweis, dass die Dokumentation als eigenständige Richtlinie, als Abschnitt in einem bestehenden Dokument oder über ein ISMS-Tool strukturiert werden kann. CON.8.A12 und NET.1.2.A12 gehen zwar ebenfalls in Richtung Dokumentation, beziehen sich aber auf Software- bzw. Netzmanagement-Dokumentation und nicht allgemein auf architekturelle Verfahren und Regelungen; daher nur mittelbare Teildeckung.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.75
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A11` [Basis] Absicherung eingehender Kommunikation vom Internet in das interne Netz — _NET.1.1 Netzarchitektur und -design_
  - `CON.7.A7` [Basis] Sicherer Remote-Zugriff auf das Netz der Institution — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `CON.7.A8` [Basis] Sichere Nutzung von öffentlichen WLANs — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `NET.1.1.A10` [Basis] DMZ-Segmentierung für Zugriffe aus dem Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A18` [Standard] P-A-P-Struktur für die Internet-Anbindung — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.2.1.A15` [Hoch] Verwendung eines VPN zur Absicherung von WLANs — _NET.2.1 WLAN-Betrieb_
  - `SYS.3.1.A8` [Standard] Sicherer Anschluss von Laptops an Datennetze — _SYS.3.1 Laptops_
  - `SYS.3.2.1.A28` [Standard] Verwendung der Filteroption für Webseiten — _SYS.3.2.1 Allgemeine Smartphones und Tablets_
  - `NET.3.3.A11` [Standard] Sichere Anbindung eines externen Netzes — _NET.3.3 VPN_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A11=0.75, CON.7.A7=0.39, CON.7.A8=0.39, NET.1.1.A10=0.39, NET.1.1.A18=0.39, NET.1.1.A4=0.39, NET.2.1.A15=0.39, SYS.3.1.A8=0.39, SYS.3.2.1.A28=0.39, NET.3.3.A11=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7800 gs_ids=NET.1.1.A4;NET.1.1.A10;NET.1.1.A11;NET.1.1.A18;CON.7.A7;CON.7.A8;SYS.3.2.1.A28;NET.2.1.A15;SYS.3.1.A8
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung ARCH.2.2.1 fordert, Verbindungen über externe Netzanschlüsse architektonisch zu begrenzen, um Angriffsfläche, unerwünschte Ein-/Ausleitungen und Datenabfluss zu reduzieren. Das wird inhaltlich teilweise durch NET.1.1.A4, NET.1.1.A10, NET.1.1.A11 und NET.1.1.A18 abgedeckt, weil diese Anforderungen die Netztrennung in Zonen, die externe DMZ, den sicheren externen Zugang via VPN sowie die P-A-P-Struktur zur kontrollierten Anbindung an das Internet beschreiben. Für mobile Systeme und externe Zugänge passen CON.7.A7 und CON.7.A8, ergänzt durch SYS.3.2.1.A28, NET.2.1.A15 und SYS.3.1.A8, da diese den sicheren Fernzugriff, VPN-Nutzung und den sicheren Anschluss mobiler Endgeräte an öffentliche Netze regeln. Insgesamt decken diese GS-Anforderungen das Ziel der Einschränkung externer Verbindungen nur teilweise ab, weil sie vor allem konkrete Zugangs- und Anbindungsszenarien behandeln, nicht aber die allgemein geforderte architektonische Begrenzung aller externen Netzanschlüsse auf Segment-Ebene.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die allgemeine, abstrakte Architekturvorgabe, Verbindungen über externe Netzanschlüsse grundsätzlich zu beschränken. Insbesondere fehlen explizite Regelungen zur systematischen Begrenzung aller externen Netzanschlüsse in der Netzarchitektur unabhängig von VPN, WLAN oder speziellen mobilen Szenarien sowie eine direkte Aussage zur Vermeidung unerwünschter Ein- und Ausleitungen als generelles Designprinzip.

### ARCH.2.2.11 — Physische Segmentierung
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `INF.14.A28` [Hoch] Physische Trennung der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A32` [Hoch] Physische Trennung von Management-Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.2.A32` [Hoch] Physische Trennung des Managementnetzes — _NET.1.2 Netzmanagement_
  - `NET.1.1.A22` [Standard] Spezifikation des Segmentierungskonzepts — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A23` [Standard] Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A31` [Hoch] Physische Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A33` [Hoch] Mikrosegmentierung des Netzes — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A28=0.44, NET.1.1.A32=0.44, NET.1.1.A4=0.44, NET.1.2.A32=0.44, NET.1.1.A22=0.34, NET.1.1.A23=0.34, NET.1.1.A31=0.34, NET.1.1.A33=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.8800 gs_ids=INF.14.A28;NET.1.1.A4;NET.1.1.A32;NET.1.2.A32
[manual:gspp_compliance_v3approach] coverage=teilweise confidence=0.6711 gs_ids=NET.1.1.A31;NET.1.1.A23;NET.1.1.A33;NET.1.1.A22
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.11 fordert physische Segmentierung bzw. die physische Trennung von Netzen, um eine Umgehung der Trennung durch virtuelle Vernetzung zu vermeiden. Das wird inhaltlich durch INF.14.A28 abgedeckt, da dort GA-Netze bei erhöhtem Schutzbedarf als physisch getrennte Zonen realisiert werden sollen. NET.1.1.A4 deckt die physische Trennung von Netzsegmenten in Zonen ab und verlangt ausdrücklich eine physische Separation der Kernzonen. NET.1.1.A32 und NET.1.2.A32 behandeln ebenfalls die physische Trennung von Management-Netzsegmenten bzw. des Managementnetzes und entsprechen damit dem Kernaspekt der physischen Segmentierung. Zusammen bilden diese Anforderungen die wesentlichen Aspekte der GS++-Anforderung ab: physische Trennung statt nur logischer Segmentierung und Schutz vor Umgehung über virtuelle Netze.
- **Lücken:** [gpt-5.4-mini] Keine wesentlichen Lücken; die Kandidaten decken den physischen Trennungsaspekt ausreichend ab. Die GS++-Hinweise zur bevorzugten physischen gegenüber virtueller Segmentierung sind implizit enthalten, aber nicht immer mit derselben allgemeinen Formulierung.

### ARCH.2.2.8 — Segmentierung von Test und Betrieb
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `APP.4.4.A1` [Basis] Planung der Separierung der Anwendungen — _APP.4.4 Kubernetes_
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.4.2.A16` [Hoch] Trennung des Daten- und VoIP-Netzes — _NET.4.2 VoIP_
  - `OPS.1.1.6.A13` [Standard] Trennung der Testumgebung von der Produktivumgebung — _OPS.1.1.6 Software-Tests und -Freigaben_
  - `SYS.1.7.A33` [Hoch] Trennung von Test- und Produktionssystemen unter z/OS — _SYS.1.7 IBM Z_
- **Begründung:** Gemittelte Kandidatenscores: APP.4.4.A1=0.46, INF.14.A6=0.46, NET.4.2.A16=0.46, OPS.1.1.6.A13=0.46, SYS.1.7.A33=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9100 gs_ids=OPS.1.1.6.A13;SYS.1.7.A33;APP.4.4.A1;INF.14.A6;NET.4.2.A16
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.8 fordert, Verbindungen zwischen Testumgebungen und Betrieb einzuschränken bzw. Test und Produktivbetrieb zu segmentieren. Dies wird inhaltlich direkt durch OPS.1.1.6.A13 abgedeckt, da dort die Trennung der Testumgebung von der Produktivumgebung gefordert wird. SYS.1.7.A33 deckt denselben Kernaspekt ebenfalls ab, allerdings spezifisch für z/OS, nämlich die technische Trennung von Entwicklungs-/Testsystemen und Produktionssystemen. APP.4.4.A1 adressiert die Separierung von Test- und Produktions-Betriebsumgebungen in Kubernetes inklusive Architektur- und Netzseparierung. INF.14.A6 ist einschlägig, weil es die logische Trennung von Netzen sowie die kontrollierte Kommunikation zwischen Segmenten verlangt; das trifft den Netzsegmentierungsaspekt der Anforderung. NET.4.2.A16 passt ebenfalls, da dort das VoIP-Netz vom Datennetz zu trennen und die zulässigen Verbindungen zu beschränken sind; das ist eine spezielle Form der Segmentierung zwischen Netzbereichen. Zusammengenommen decken diese Anforderungen den wesentlichen Inhalt der GS++-Anforderung ab.
- **Lücken:** [gpt-5.4-mini] Die Kandidaten enthalten keine generische, bausteinübergreifende Anforderung speziell für Test-vs.-Betrieb auf reiner Netzwerkebene; die Abdeckung ergibt sich aus mehreren, domänennahen Einzelanforderungen. Spezifische Aspekte wie Ressourcenkonflikte zwischen Test und Produktivbetrieb werden nur indirekt adressiert.

### ARCH.2.2.9 — Segmentierung von IPv4 und IPv6
- **Confidence:** 0.37
- **Gemappte GS-Anforderungen:**
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A20` [Standard] Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A17` [Standard] Deaktivierung von IPv4 oder IPv6 — _NET.3.2 Firewall_
  - `NET.4.2.A16` [Hoch] Trennung des Daten- und VoIP-Netzes — _NET.4.2 VoIP_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.37, NET.1.1.A20=0.37, NET.3.2.A17=0.37, NET.4.2.A16=0.37
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7400 gs_ids=NET.1.1.A20;NET.3.2.A17;NET.4.2.A16;INF.14.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.1.1.A20 adressiert die Trennung nach IPv4-/IPv6-Endgerätegruppen in dedizierte Subnetze und trifft damit einen Teil des Ziels, Verbindungen zwischen IPv4 und IPv6 zu begrenzen. NET.3.2.A17 geht in dieselbe Richtung, indem ein nicht benötigtes IPv4- oder IPv6-Protokoll an einem Netzsegment bzw. Firewall-Übergang deaktiviert wird. NET.4.2.A16 beschreibt zwar die Trennung eines VoIP-Netzes vom Datennetz und damit Segmentierung, ist aber auf VoIP spezialisiert und nicht auf IPv4/IPv6-bezogene Verbindungen. INF.14.A6 fordert eine logische Trennung und kontrollierte Kommunikation zwischen Netzen, was den generellen Segmentierungsgedanken unterstützt. Zusammen decken diese Anforderungen die allgemeine Einschränkung von Verbindungen zwischen Segmenten nur teilweise ab, aber nicht die spezifische Zielsetzung der GS++-Anforderung, IPv4- und IPv6-Umgebungen bzw. deren Wechselwirkungen gezielt voneinander zu trennen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die explizite, protokollspezifische Segmentierung bzw. Einschränkung von Verbindungen zwischen IPv4- und IPv6-Netzen als Schutz vor Wechselwirkungen und Protokollkombinationen. NET.1.1.A20 behandelt primär die Subnetzzuordnung von Endgeräten, NET.3.2.A17 die Deaktivierung nicht benötigter Protokolle, INF.14.A6 und NET.4.2.A16 sind domänen- bzw. zweckgebunden allgemeiner Segmentierung. Eine konkrete Anforderung, IPv4 und IPv6 grundsätzlich voneinander zu trennen oder ihre Kommunikation gezielt zu beschränken, fehlt.

### ARCH.5.1.12 — Software-definierte Verbindungen
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A2` [Basis] Festlegen der Firewall-Regeln — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A2=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=NET.3.2.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A2 passt inhaltlich, weil die Anforderung die Steuerung und Unterbindung von Kommunikationsverbindungen zwischen Netzen über Firewall-Regeln regelt und damit grundsätzlich die Einschränkung von Verbindungen adressiert. Die GS++-Anforderung ARCH.5.1.12 verlangt jedoch ausdrücklich eine Einschränkung anhand dynamischer Kriterien bzw. kontextabhängiger Bewertung (z. B. device posture, Auslastung, Standort, Risikobewertung, adaptive Policy-Engines/SDN). Diese dynamische, kontextbasierte Regelungslogik wird in NET.3.2.A2 nicht beschrieben; dort geht es nur um statische, fest definierte Allowlist-Regeln für Verbindungen.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die dynamische Bewertung von Verbindungen anhand aktueller Kontextmerkmale, die adaptive/kontextabhängige Policy-Entscheidung sowie die explizite Verwendung von SDN-, Mikrosegmentierungs- oder Policy-Engine-Mechanismen. NET.3.2.A2 deckt nur statische Firewall-Regelung ab.

### ARCH.5.1.8 — Inspektion verschlüsselter Verbindungen
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A21` [Standard] Temporäre Entschlüsselung des Datenverkehrs — _NET.3.2 Firewall_
  - `NET.3.2.A28` [Hoch] Zentrale Filterung von aktiven Inhalten — _NET.3.2 Firewall_
  - `NET.1.1.A12` [Basis] Absicherung ausgehender interner Kommunikation zum Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A20` [Standard] Absicherung von grundlegenden Internetprotokollen — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A21=0.43, NET.3.2.A28=0.43, NET.1.1.A12=0.34, NET.3.2.A20=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=NET.3.2.A28;NET.3.2.A21
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6855 gs_ids=NET.3.2.A20;NET.1.1.A12
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A28 deckt die zentrale Filterung aktiver Inhalte und ausdrücklich die Entschlüsselung verschlüsselten Datenverkehrs über Sicherheitsproxies ab, was der Inspektion verschlüsselter Verbindungen inhaltlich nahekommt. NET.3.2.A21 ergänzt dies um die temporäre Entschlüsselung verschlüsselter Verbindungen in nicht vertrauenswürdige Netze zur Protokollverifikation und Schadsoftwareprüfung. Zusammen adressieren beide Kandidaten den Kernaspekt der Entschlüsselung/Inspektion verschlüsselter Verbindungen. Die GS++-Anforderung fordert jedoch breiter, dass die Architektur für externe Netzanschlüsse den Inhalt unverschlüsselter und verschlüsselter Verbindungen basierend auf der Inhaltsart einschränken soll; diese allgemeine, architekturbezogene Inhaltsrestriktion ist in den Kandidaten nicht vollständig enthalten.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine Architekturvorgabe zur inhaltsabhängigen Einschränkung aller externen Netzverbindungen sowie die explizite Beschränkung sowohl unverschlüsselter als auch verschlüsselter Verbindungen nach Inhaltsart. Außerdem ist die GS++-Anforderung breiter auf Inspektion als Designprinzip für externe Netzanschlüsse ausgerichtet, während die Kandidaten primär konkrete technische Entschlüsselungs-/Proxy-Maßnahmen beschreiben.

### ASST.2.1.1 — Informationsverantwortung
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `ORP.1.A2` [Basis] Zuweisung der Zuständigkeiten — _ORP.1 Organisation_
- **Begründung:** Gemittelte Kandidatenscores: ORP.1.A2=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9200 gs_ids=ORP.1.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.1.A2 passt inhaltlich am ehesten, weil dort für Geschäftsprozesse, Anwendungen, IT-Systeme, Räume, Gebäude und Kommunikationsverbindungen festgelegt werden muss, wer zuständig ist, und die Mitarbeitenden über ihre Zuständigkeiten informiert werden. Das deckt den Aspekt der eindeutigen Zuständigkeitszuweisung ab. Die GS++-Anforderung ASST.2.1.1 geht jedoch spezifischer auf die Zuständigkeit für die Verarbeitung von Informationen und Assets im Sinne von Asset Ownership ein; diese explizite Zuordnung zu Informationen bzw. Daten ist in ORP.1.A2 nicht vollständig enthalten.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die explizite Informationsverantwortung für die Verarbeitung konkreter Informationen und Assets (Asset Ownership). ORP.1.A2 regelt allgemeine Zuständigkeiten für Prozesse, Systeme und andere Objekte, aber nicht die spezifische Zuständigkeit für Informationsbestände oder deren Schutz im Rahmen der Verarbeitung.

### ASST.2.2.1 — Aufdecken unautorisierter IT-Systeme
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.1.A6` [Standard] Durchführung des IT-Asset-Managements — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `OPS.3.2.A14` [Standard] Überwachung der Prozesse, Anwendungen und IT-Systeme — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.1.A6=0.44, OPS.3.2.A14=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=OPS.1.1.1.A6;OPS.3.2.A14
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.1.A6 passt inhaltlich, weil die Anforderung ein vollständiges, aktuelles IT-Asset-Management mit regelmäßiger Prüfung der vorhandenen IT-Assets verlangt. Damit wird das Erkennen unbekannter bzw. nicht autorisierter Systeme organisatorisch unterstützt, jedoch nicht explizit das aktive Aufdecken im Netz. OPS.3.2.A14 passt ebenfalls teilweise, weil die kontinuierliche Überwachung von Prozessen, Anwendungen und IT-Systemen eine technische/organisatorische Grundlage für das Erkennen unautorisierter Systeme sein kann. Beide Anforderungen behandeln aber eher Inventarisierung bzw. Monitoring allgemein und nicht spezifisch das gezielte Aufdecken unautorisierter IT-Systeme mittels Scans, passiver Analyse oder WLAN-Erkennung.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkreten Erkennungsverfahren (aktive Netzscans, passive Traffic-Analyse, Spezialwerkzeuge wie Kismet), die explizite Fokussierung auf unautorisierte Assets im Informationsverbund sowie mögliche Folgebehandlungen wie Quarantäne, Entfernen aus dem Netz oder Autorisierung nach Prüfung.

### ASST.4.4 — Nachweis des Zugangs
- **Confidence:** 0.41
- **Gemappte GS-Anforderungen:**
  - `DER.3.1.A27` [Standard] Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen — _DER.3.1 Audits und Revisionen_
  - `NET.4.2.A12` [Standard] Sichere Außerbetriebnahme von VoIP-Komponenten — _NET.4.2 VoIP_
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.3.2.A6` [Basis] Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: DER.3.1.A27=0.41, NET.4.2.A12=0.41, OPS.2.3.A7=0.41, OPS.3.2.A6=0.41
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8300 gs_ids=DER.3.1.A27;OPS.3.2.A6;OPS.2.3.A7;NET.4.2.A12
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.3.1.A27 passt inhaltlich, weil dort die nachvollziehbare und revisionssichere Aufbewahrung von Unterlagen zu Audits und Revisionen geregelt ist; damit wird der Aspekt der archivierten Nachweisführung für Zugänge/Erreichung im Streit- oder Prüfkontext nur teilweise berührt. OPS.3.2.A6 und OPS.2.3.A7 passen teilweise, weil sie die dokumentierte Rückgabe von Informationen/Daten und die Prüfung der Aufhebung von Rechten bei Beendigung von Outsourcing regeln; ein echter Zugangsnachweis für den Empfänger oder eine protokollierte Empfangsbestätigung wird jedoch nicht gefordert. NET.4.2.A12 passt ebenfalls nur teilweise, da nach dem Löschvorgang die erfolgreiche Entfernung sicherheitsrelevanter Informationen überprüft werden soll; das ist eine Erfolgs-/Löschkontrolle, aber kein Nachweis, dass eine Nachricht ihren Empfänger tatsächlich erreicht hat.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind insbesondere der eigentliche Zugangsnachweis an den Empfänger, die protokollierte Empfangsbestätigung mit Zeitstempel, Versand- und Zieladressen sowie ggf. Inhalt der Nachricht. Auch die manipulationssichere Archivierung eines solchen Empfangsnachweises über definierte Aufbewahrungsfristen wird von den Kandidaten nicht ausdrücklich gefordert.

### ASST.6.1 — Abhandenkommen
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `DER.2.1.A6` [Basis] Wiederherstellung der Betriebsumgebung nach Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `DER.2.1.A7` [Standard] Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `SYS.3.1.A12` [Standard] Verlustmeldung für Laptops — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.1.A6=0.45, DER.2.1.A7=0.45, SYS.3.1.A12=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9000 gs_ids=SYS.3.1.A12;DER.2.1.A7;DER.2.1.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] SYS.3.1.A12 deckt den konkreten Fall des Verlusts oder Diebstahls eines Laptops einschließlich Meldewegen, Untersuchung bei Wiederauftauchen und Neuinstallation ab. DER.2.1.A7 deckt die allgemeine, dokumentierte Vorgehensweise zur Behandlung von Sicherheitsvorfällen ab und passt damit zur geforderten strukturierten Reaktion auf Verlustereignisse. DER.2.1.A6 ergänzt die Sofortmaßnahmen nach einem Sicherheitsvorfall, insbesondere Netztrennung, Sicherung relevanter Daten und Änderung von Zugangsdaten. Zusammen bilden die Anforderungen wesentliche Teile einer Vorgehensweise beim Abhandenkommen von Assets ab.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind asset-übergreifende Vorgaben für alle Informationswerte und Assets, insbesondere spezifische Maßnahmen wie Ortung, Fernsperrung/-löschung für unterschiedliche Asset-Typen, Meldung an Behörden/Fundbüros sowie die Sperre von Authentisierungsmitteln und SIM-Karten außerhalb des Mobiltelefon-Kontexts. Die Kandidaten fokussieren überwiegend auf Sicherheitsvorfälle bzw. Laptop/Mobiltelefon, nicht auf eine allgemeine Asset-Verlustprozedur.

### ASST.7.1 — Nicht mehr benötigte Anwendungen
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `APP.6.A13` [Standard] Deinstallation von Software — _APP.6 Allgemeine Software_
  - `SYS.1.9.A15` [Standard] Härtung des Terminalservers — _SYS.1.9 Terminalserver_
  - `SYS.2.1.A16` [Standard] Deaktivierung und Deinstallation nicht benötigter Komponenten und Kennungen — _SYS.2.1 Allgemeiner Client_
  - `SYS.3.2.2.A7` [Standard] Installation von Apps — _SYS.3.2.2 Mobile Device Management (MDM)_
  - `SYS.4.4.A13` [Standard] Deaktivierung und Deinstallation nicht benötigter Komponenten — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.6.A13=0.46, SYS.1.9.A15=0.46, SYS.2.1.A16=0.46, SYS.3.2.2.A7=0.46, SYS.4.4.A13=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9200 gs_ids=APP.6.A13;SYS.1.9.A15;SYS.2.1.A16;SYS.3.2.2.A7;SYS.4.4.A13
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Anforderungen APP.6.A13, SYS.1.9.A15, SYS.2.1.A16, SYS.3.2.2.A7 und SYS.4.4.A13 decken jeweils das Entfernen bzw. Deinstallieren nicht mehr benötigter Software oder Komponenten in konkreten technischen Umgebungen ab. APP.6.A13 fordert bei der Deinstallation von Software das Entfernen nicht mehr benötigter Dateien und Systemeinträge; SYS.1.9.A15 verlangt, nicht benötigte Anwendungen auf dem Terminalserver zu entfernen; SYS.2.1.A16 verlangt für Clients die Deaktivierung bzw. Deinstallation nicht benötigter Programme, Dienste und Kennungen; SYS.3.2.2.A7 regelt die Installation, Deinstallation und Aktualisierung von Apps über MDM; SYS.4.4.A13 fordert für IoT-Geräte die Deaktivierung oder Deinstallation nicht benötigter Protokolle, Dienste, Anmeldekennungen und Schnittstellen. Damit ist der Kernaspekt der GS++-Anforderung ASST.7.1 — die Deinstallation nicht mehr benötigter Anwendungsinstanzen — inhaltlich gut getroffen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die ASST-spezifischen Aspekte: geregelter institutioneller Prozess für das Ende von Anwendungsinstanzen über alle Umgebungen hinweg, vollständige und nachvollziehbare Entfernung inklusive zugehöriger Berechtigungen/Zugriffsrechte, sowie Cloud-spezifisch das Löschen von Daten bei nicht unter eigener Kontrolle stehenden Instanzen. Außerdem adressieren die Kandidaten primär technische Einzelumgebungen, nicht die übergreifende Asset-/Anwendungslebenszyklus-Regelung der GS++-Anforderung.

### ASST.7.6 — Autorisierung von Veräußerungen
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `CON.6.A1` [Basis] Regelung für die Löschung und Vernichtung von Informationen — _CON.6 Löschen und Vernichten_
  - `CON.6.A2` [Basis] Ordnungsgemäßes Löschen und Vernichten von schützenswerten Betriebsmitteln und Informationen — _CON.6 Löschen und Vernichten_
  - `CON.6.A8` [Standard] Erstellung einer Richtlinie für die Löschung und Vernichtung von Informationen — _CON.6 Löschen und Vernichten_
- **Begründung:** Gemittelte Kandidatenscores: CON.6.A1=0.46, CON.6.A2=0.46, CON.6.A8=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9100 gs_ids=CON.6.A1;CON.6.A8;CON.6.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.6.A1, CON.6.A8 und CON.6.A2 decken den Kernaspekt der Lösch- und Vernichtungsregelung vor der Entsorgung bzw. dem Austritt von Informationen/Datenträgern ab. CON.6.A2 verlangt, dass schutzbedürftige Informationen und Datenträger vor der Entsorgung sicher gelöscht oder vernichtet werden und dass der Prozess klar geregelt ist. CON.6.A1 fordert eine institutionelle Regelung des Löschens und Vernichtens von Informationen inklusive fachlicher Festlegungen und Beachtung gesetzlicher Vorgaben. CON.6.A8 ergänzt die dokumentierte Richtlinie für Löschung und Vernichtung. Damit ist die in ASST.7.6 geforderte Autorisierung von Veräußerungen jedoch nicht vollständig abgedeckt, da die GS-Anforderungen die explizite Freigabe/Genehmigung der Veräußerung durch definierte Rollen, einen Freigabe-Workflow oder eine Entscheidungsmatrix nicht regeln, sondern primär das sichere Löschen/Vernichten vor der Entsorgung behandeln.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die eigentliche Autorisierung der Veräußerung als separater Freigabeprozess, die Festlegung von Genehmigungsrollen je Schutzbedarf, die revisionssichere Dokumentation des Veräußerungsantrags sowie die Behandlung von Lizenz-/Vertragsübertragungen und Empfängern. Abgedeckt ist nur der Vorab-Aspekt des sicheren Löschens/Vernichtens vor Abgabe oder Entsorgung.

### BER.1.1.3 — Bekanntgabe
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `APP.5.4.A5` [Basis] Rollen- und Berechtigungskonzept für UCC — _APP.5.4 Unified Communications und Collaboration (UCC)_
  - `OPS.1.1.3.A11` [Standard] Kontinuierliche Dokumentation der Informationsverarbeitung — _OPS.1.1.3 Patch- und Änderungsmanagement_
  - `OPS.1.2.5.A6` [Standard] Erstellung einer Richtlinie für die Fernwartung — _OPS.1.2.5 Fernwartung_
- **Begründung:** Gemittelte Kandidatenscores: APP.5.4.A5=0.45, OPS.1.1.3.A11=0.45, OPS.1.2.5.A6=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=OPS.1.1.3.A11;OPS.1.2.5.A6;APP.5.4.A5
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.3.A11 deckt den Kernaspekt ab, dass Änderungen und damit verbundene Regelungen dokumentiert werden sollen. OPS.1.2.5.A6 passt, weil dort eine Richtlinie zur Fernwartung zu erstellen ist, die allen Zuständigen bekannt sein soll; das entspricht dem Informationsaspekt für Beteiligte. APP.5.4.A5 ergänzt dies, da Rollen- und Berechtigungskonzepte festgehalten, regelmäßig geprüft und aktualisiert werden müssen. Gemeinsam wird damit die Dokumentation und teilweise die Bekanntgabe von Verfahren/Regelungen an zuständige Rollen adressiert.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die explizite Pflicht, die zuständigen Personen oder Rollen aktiv über die Verfahren und Regelungen zu informieren, insbesondere anlassbezogen bzw. automatisch bei Änderungen. Die Kandidaten sprechen eher von Dokumentation, Bekanntheit oder Aktualisierung, aber nicht in voller Breite von strukturierten Bekanntgabe-/Benachrichtigungsprozessen (z. B. Onboarding und automatische Änderungsbenachrichtigung).

### BER.1.2 — Regelmäßige Überprüfung
- **Confidence:** 0.39
- **Gemappte GS-Anforderungen:**
  - `DER.1.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `DER.1.A13` [Standard] Regelmäßige Audits der Detektionssysteme — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `DER.4.A14` [Hoch] Regelmäßige Überprüfung und Verbesserung der Notfallmaßnahmen — _DER.4 Notfallmanagement_
  - `INF.1.A36` [Standard] Regelmäßige Aktualisierungen der Dokumentation — _INF.1 Allgemeines Gebäude_
  - `OPS.1.1.1.A2` [Basis] Festlegung von Rollen und Berechtigungen für den IT-Betrieb — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `ORP.5.A8` [Standard] Regelmäßige Überprüfungen des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `SYS.3.2.2.A20` [Basis] Regelmäßige Überprüfung des MDM — _SYS.3.2.2 Mobile Device Management (MDM)_
  - `APP.4.3.A20` [Standard] Regelmäßige Audits — _APP.4.3 Relationale Datenbanken_
  - `OPS.1.2.2.A13` [Standard] Regelmäßige Revision der Archivierungsprozesse — _OPS.1.2.2 Archivierung_
- **Begründung:** Gemittelte Kandidatenscores: DER.1.A1=0.39, DER.1.A13=0.39, DER.4.A14=0.39, INF.1.A36=0.39, OPS.1.1.1.A2=0.39, ORP.5.A8=0.39, SYS.3.2.2.A20=0.39, APP.4.3.A20=0.33, OPS.1.2.2.A13=0.33
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7800 gs_ids=ORP.5.A8;DER.4.A14;DER.1.A13;DER.1.A1;INF.1.A36;OPS.1.1.1.A2;SYS.3.2.2.A20
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6600 gs_ids=APP.4.3.A20;OPS.1.2.2.A13
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung BER.1.2 verlangt die regelmäßige sowie anlassbezogene Überprüfung von Verfahren und Regelungen auf Aktualität. Inhaltlich passen dazu vor allem ORP.5.A8, DER.4.A14, DER.1.A13, DER.1.A1 und INF.1.A36, da sie jeweils explizit regelmäßige Überprüfungen von Management-, Notfall-, Detektions- oder Dokumentationsregelungen fordern und die Aktualität/Wirksamkeit der Regelungen adressieren. OPS.1.1.1.A2 und SYS.3.2.2.A20 enthalten ebenfalls regelmäßige Überprüfungen von Rollen, Berechtigungen bzw. Sicherheitseinstellungen; das trifft den Aspekt der periodischen Aktualitätsprüfung von Regelungen teilweise. Die Anforderungen sind jedoch überwiegend domänenspezifisch (Compliance, Notfall, Detektion, MDM, IT-Betriebsberechtigungen) und decken nicht die allgemein formulierte BER-Anforderung für Berechtigung vollständig ab.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind der allgemeine, domänenübergreifende Charakter der Überprüfung von Verfahren und Regelungen im Berechtigungsmanagement sowie die explizite anlassbezogene Überprüfung bei Ereignissen wie Sicherheitsvorfällen, strategischen Änderungen oder neuen gesetzlichen Vorgaben. Die Kandidaten fokussieren eher einzelne Fachbereiche und nennen die anlassbezogene Triggerung nur teilweise bzw. nicht in der erforderlichen Allgemeinheit.

### BER.2.5 — Deaktivierung bei Weggang
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `DER.3.1.A24` [Standard] Abschluss des Audits oder der Revision — _DER.3.1 Audits und Revisionen_
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.3.2.A6` [Basis] Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.3.2 Anbieten von Outsourcing_
  - `ORP.2.A2` [Basis] Geregelte Verfahrensweise beim Weggang von Mitarbeitenden — _ORP.2 Personal_
- **Begründung:** Gemittelte Kandidatenscores: DER.3.1.A24=0.44, OPS.2.3.A7=0.44, OPS.3.2.A6=0.44, ORP.2.A2=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=OPS.2.3.A7;OPS.3.2.A6;ORP.2.A2;DER.3.1.A24
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.2.3.A7 und OPS.3.2.A6 decken den organisatorischen Teil der Beendigung eines Outsourcing-Verhältnisses ab, insbesondere das Aufheben von Zugangs-, Zutritts- und Zugriffsrechten nach Vertragsende. ORP.2.A2 ist ebenfalls passend, weil dort beim Weggang von Mitarbeitenden ausdrücklich das Einziehen von Ausweisen und Zutrittsberechtigungen sowie die Information betroffener Stellen geregelt wird. DER.3.1.A24 ergänzt den Aspekt der Rückgabe bzw. Löschung genehmigter Zugriffe nach Abschluss eines Audits und ist inhaltlich nah an der Deaktivierung von Identitäten nach Weggang, aber nicht identisch.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die Kernaspekte der GS++-Anforderung: Die gezielte Deaktivierung oder Löschung der zugeordneten Identität selbst bei Weggang von Nutzenden wird in den Kandidaten nicht explizit gefordert. OPS.2.3.A7 und OPS.3.2.A6 beziehen sich auf Outsourcing-Verhältnisse, nicht allgemein auf Mitarbeitenden-Identitäten. ORP.2.A2 fordert das Einziehen von Ausweisen und Zutrittsberechtigungen, aber keine Deaktivierung von IT-Identitäten. Die Löschung mit Blick auf Audit-Log-Nachvollziehbarkeit wird ebenfalls nicht behandelt.

### BER.3.15 — Keine Gruppenkonten
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `SYS.2.4.A3` [Basis] Verwendung geeigneter Konten — _SYS.2.4 Clients unter macOS_
- **Begründung:** Gemittelte Kandidatenscores: SYS.2.4.A3=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9000 gs_ids=SYS.2.4.A3
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] SYS.2.4.A3 deckt den Kernaspekt der Anforderung BER.3.15 ab, weil dort für die normale Nutzung ein eigenes Konto je Benutzendem gefordert wird und das Gast-Konto zu deaktivieren ist. Damit wird die Mehrfachnutzung eines Zugangskontos durch mehrere Personen im Sinn der Anforderung vermieden. Die GS++-Anforderung ist jedoch allgemeiner formuliert und verbietet Gruppenkonten grundsätzlich für Berechtigungskonzepte; die Kandidatenanforderung adressiert nur den Fall der macOS-Nutzung und nicht generell alle Kontenarten und Anwendungskontexte.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind der allgemeine, bausteinübergreifende Verzicht auf Gruppenkonten sowie die explizite Untersagung von gemeinsam genutzten Zugangskonten unabhängig von Plattform oder Einsatzszenario. Außerdem wird die organisatorische Regelung auf Berechtigungsebene nicht generell beschrieben, sondern nur für macOS-Endgeräte.

### BER.7.16.6 — Revocationstatus
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `DER.2.3.A4` [Basis] Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln — _DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.3.A4=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9300 gs_ids=DER.2.3.A4
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.2.3.A4 passt inhaltlich, weil dort nach einer Kompromittierung explizit gefordert wird, kompromittierte Schlüssel und Zertifikate zuverlässig zu sperren und zurückzurufen. Das entspricht dem Kern des GS++-Texts, der den Revocationstatus eines Schlüssels dokumentieren bzw. den zurückgezogenen Status im Verzeichnis öffentlicher Schlüssel abbilden will. Die Forderung von DER.2.3.A4 ist jedoch stärker auf operative Reaktion nach Sicherheitsvorfällen ausgerichtet und enthält keine explizite Vorgabe zur Dokumentation des Revocationstatus im Public-Key-Verzeichnis; daher nur teilweise.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die explizite Dokumentation des Revocationstatus im Verzeichnis öffentlicher Schlüssel sowie die allgemeinere Vorgabe zur Pflege dieses Status als Verzeichnisattribut außerhalb des Vorfallskontextes.

## Keine Abdeckung (2)

### BER.6.8 — Kriterien für die Qualität von Passwörtern
- **Confidence:** 0.47
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9300 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidatenanforderungen behandelt die Festlegung von Kriterien für die Qualität von Passwörtern anhand von Lebensdauer, Entropie, Passwortlänge oder Angriffsmöglichkeiten. Die Kandidaten zu Mehr-Faktor-Authentisierung (CON.10.A16, ORP.4.A21, SYS.2.1.A37, OPS.1.2.5.A17) betreffen eine andere Schutzmaßnahme als Passwortqualitätsregeln. ORP.4.A11 regelt das sichere Zurücksetzen von Passwörtern, aber nicht deren Qualitätskriterien. CON.1.A9 und CON.1.A10 betreffen Kryptokonzepte bzw. Kriterien für kryptografische Hard-/Software, nicht Passwortqualität. Die übrigen Kandidaten sind fachlich ebenfalls nicht passend.
- **Lücken:** [gpt-5.4-mini] Es fehlt eine Anforderung zur Festlegung und ggf. Differenzierung von Passwortqualitätskriterien (z. B. Mindestlänge, Entropie, erlaubte Zeichen, Abhängigkeit von Schutzbedarf, Lebensdauer und Angriffsmöglichkeiten). Auch die Empfehlung, Passwortregeln an begleitende Maßnahmen wie maximale Fehlversuche oder MFA anzupassen, wird nicht abgedeckt.

### BER.7.16.3 — Erneuerung
- **Confidence:** 0.47
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9300 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidaten beschreibt die Prüfung eines Schlüssels im Rahmen der Erneuerung einer Beglaubigung/Zertifikats-erneuerung mit Fokus auf Verifikation der Schlüsselgültigkeit, Signaturprüfung, Fingerprint-Abgleich oder Sperrlistenprüfung. CON.1.A4 regelt zwar allgemeines Schlüsselmanagement, Authentizität und rechtzeitige Erneuerung ablaufender Zertifikate, aber nicht die geforderte spezifische Schlüsselprüfung bei der Erneuerung. DER.2.3.A4 behandelt die Reaktion auf kompromittierte TLS-Schlüssel bzw. CA, also Neuaufbau und Sperrung nach Vorfall, nicht die reguläre Erneuerungsprüfung. Die übrigen Kandidaten sind thematisch weiter entfernt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkrete Verifikation des Schlüssels bei Zertifikats-/Beglaubigungserneuerung und die dabei genannten Prüfarten (Signatur, Fingerprint, Sperrlisten/Revocation-Checks). Allgemeines Schlüsselmanagement oder Neuausstellung nach Kompromittierung reicht hierfür nicht aus.
