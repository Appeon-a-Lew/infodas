# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:59:23

**Gesamt:** 20 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 19 |
| Keine Abdeckung | 1 |

## Teilweise abgedeckt (19)

### ARCH.1.1.1 — Dokumentation
- **Confidence:** 0.35
- **Gemappte GS-Anforderungen:**
  - `APP.2.1.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für Verzeichnisdienste — _APP.2.1 Allgemeiner Verzeichnisdienst_
  - `APP.6.A10` [Standard] Erstellung einer Sicherheitsrichtlinie für den Einsatz der Software — _APP.6 Allgemeine Software_
  - `APP.7.A6` [Standard] Dokumentation der Anforderungen an die Individualsoftware — _APP.7 Entwicklung von Individualsoftware_
  - `CON.10.A11` [Standard] Softwarearchitektur einer Webanwendung — _CON.10 Entwicklung von Webanwendungen_
  - `CON.8.A12` [Standard] Ausführliche Dokumentation — _CON.8 Software-Entwicklung_
  - `DER.3.1.A6` [Standard] Definition der Prüfungsgrundlage und eines einheitlichen Bewertungsschemas — _DER.3.1 Audits und Revisionen_
  - `DER.4.A12` [Hoch] Dokumentation im Notfallmanagement-Prozess — _DER.4 Notfallmanagement_
  - `IND.1.A11` [Standard] Sichere Beschaffung und Systementwicklung — _IND.1 Prozessleit- und Automatisierungstechnik_
  - `IND.2.7.A1` [Basis] Erfassung und Dokumentation — _IND.2.7 Safety Instrumented Systems_
  - `NET.1.2.A12` [Standard] Ist-Aufnahme und Dokumentation des Netzmanagements — _NET.1.2 Netzmanagement_
  - `SYS.1.1.A11` [Standard] Festlegung einer Sicherheitsrichtlinie für Server — _SYS.1.1 Allgemeiner Server_
  - `SYS.4.4.A6` [Standard] Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.2.1.A1=0.35, APP.6.A10=0.35, APP.7.A6=0.35, CON.10.A11=0.35, CON.8.A12=0.35, DER.3.1.A6=0.35, DER.4.A12=0.35, IND.1.A11=0.35, IND.2.7.A1=0.35, NET.1.2.A12=0.35, SYS.1.1.A11=0.35, SYS.4.4.A6=0.35
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7100 gs_ids=APP.6.A10;CON.8.A12;DER.4.A12;NET.1.2.A12;IND.1.A11;APP.7.A6;CON.10.A11;SYS.1.1.A11;SYS.4.4.A6;APP.2.1.A1;DER.3.1.A6;IND.2.7.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.1.1.1 verlangt die Dokumentation von Verfahren und Regelungen auf einer übergeordneten organisatorischen Ebene. Inhaltlich am nächsten liegen die Kandidaten APP.6.A10, APP.2.1.A1, SYS.1.1.A11 und SYS.4.4.A6, weil sie jeweils verlangen, Regeln/Richtlinien für den Einsatz bzw. Betrieb zu erstellen, bekannt zu machen und teils zu dokumentieren. CON.8.A12, CON.10.A11, APP.7.A6, NET.1.2.A12, IND.1.A11 und IND.2.7.A1 decken den Dokumentationsaspekt für Architektur-, Entwicklungs-, Netz- bzw. Anlagenkontexte ab. DER.4.A12 und DER.3.1.A6 betreffen die Dokumentation von Prozessen bzw. Audit-Bewertungsvorgaben, also ebenfalls eine formalisierte Dokumentation von Regelwerken und Abläufen. Insgesamt besteht aber keine einzelne und auch keine Kombination, die die allgemeine Anforderung vollständig abdeckt, weil die Kandidaten jeweils auf spezielle Domänen oder einzelne Regelungsarten begrenzt sind und nicht die generelle, institutionenweite Dokumentation von Verfahren und Regelungen als übergreifende Anforderung beschreiben.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine, domänenunabhängige Dokumentation aller relevanten Verfahren und Regelungen sowie die explizite Ausrichtung an Management- und Umsetzungsrollen. Die Kandidaten behandeln überwiegend spezifische Fachdomänen (Software, Netz, Server, IoT, OT, Audit, Notfallmanagement) oder die Erstellung einzelner Richtlinien, aber keine allgemeine, institutionenweite Dokumentationspflicht für alle architektonischen Verfahren und Regelungen.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.79
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A11` [Basis] Absicherung eingehender Kommunikation vom Internet in das interne Netz — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A10` [Basis] DMZ-Segmentierung für Zugriffe aus dem Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A18` [Standard] P-A-P-Struktur für die Internet-Anbindung — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A9` [Basis] Grundlegende Absicherung der Kommunikation mit nicht vertrauenswürdigen Netzen — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.3.A11` [Standard] Sichere Anbindung eines externen Netzes — _NET.3.3 VPN_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A11=0.79, NET.1.1.A10=0.43, NET.1.1.A18=0.43, NET.1.1.A4=0.43, NET.1.1.A9=0.43, NET.3.3.A11=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8700 gs_ids=NET.1.1.A10;NET.1.1.A4;NET.1.1.A9;NET.1.1.A18;NET.1.1.A11
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.1 verlangt, dass die Architektur für Netze Verbindungen über externe Netzanschlüsse einschränkt, um Angriffsfläche, unerwünschte Ein-/Ausleitungen und Datenabfluss zu reduzieren. Das wird inhaltlich durch NET.1.1.A4 (Zonentrennung und Firewall-Absicherung), NET.1.1.A9 (Einstufung nicht vertrauenswürdiger Netze und entsprechende Absicherung), NET.1.1.A10 (externe DMZ für aus dem Internet erreichbare Dienste), NET.1.1.A11 (sicherer, auf vertrauenswürdige Systeme beschränkter IP-Zugriff via VPN) und NET.1.1.A18 (P-A-P-Struktur bzw. Sicherheits-Proxies zur Entkopplung von Internetverkehr) teilweise abgedeckt. Diese Anforderungen beschreiben jedoch primär die Sicherung bzw. Segmentierung von Internet-/Netzanschlüssen und Zugängen, nicht allgemein die architektonische Einschränkung aller externen Netzanschlüsse. Insbesondere die explizite Steuerung externer Anschlüsse für mobile Systeme und die generelle Architekturregel, externe Verbindungen zu minimieren bzw. nur gezielt zuzulassen, werden nur indirekt getroffen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine architektonische Vorgabe, externe Netzanschlüsse insgesamt zu begrenzen, sowie der explizite Bezug auf mobile Systeme und alternative sichere Direktanbindung (z. B. VPN ins gefilterte Netz oder Direct-Internet-Access-Agent). Die Kandidaten behandeln vor allem Internetanbindung, DMZ, VPN und Firewall-Strukturen, aber nicht die vollständige Regelung externer Anschlusskonzepte auf Architektur-Ebene.

### ARCH.2.2.11 — Physische Segmentierung
- **Confidence:** 0.40
- **Gemappte GS-Anforderungen:**
  - `INF.14.A28` [Hoch] Physische Trennung der GA — _INF.14 Gebäudeautomation_
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A32` [Hoch] Physische Trennung von Management-Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.2.A32` [Hoch] Physische Trennung des Managementnetzes — _NET.1.2 Netzmanagement_
  - `NET.1.1.A22` [Standard] Spezifikation des Segmentierungskonzepts — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A23` [Standard] Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A31` [Hoch] Physische Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A33` [Hoch] Mikrosegmentierung des Netzes — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A28=0.40, INF.14.A6=0.40, NET.1.1.A32=0.40, NET.1.1.A4=0.40, NET.1.2.A32=0.40, NET.1.1.A22=0.34, NET.1.1.A23=0.34, NET.1.1.A31=0.34, NET.1.1.A33=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.7900 gs_ids=NET.1.1.A4;INF.14.A28;NET.1.2.A32;NET.1.1.A32;INF.14.A6
[manual:gspp_compliance_v3approach] coverage=teilweise confidence=0.6711 gs_ids=NET.1.1.A31;NET.1.1.A23;NET.1.1.A33;NET.1.1.A22
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.11 fordert die physische Segmentierung bzw. physische Trennung von Netzen, um Netztrennung nicht nur logisch/virtuell, sondern auf physischer Ebene zu erzwingen. NET.1.1.A4 deckt die physische Trennung von Netz-Zonen (intern, DMZ, Außenanbindungen) als grundlegendes Netzdesign ab und passt damit direkt zum Kernaspekt. INF.14.A28 überträgt denselben Gedanken auf GA-Netze und verlangt bei erhöhtem Schutzbedarf physisch getrennte Zonen; damit ist die physische Segmentierung in einem konkreten Anwendungsbereich abgedeckt. NET.1.2.A32 fordert die physische Trennung des Managementnetzes von produktiven Netzen und adressiert ebenfalls die physische Segmentierung von Netzbereichen. NET.1.1.A32 verlangt die physische Trennung von Management-Netzsegmenten innerhalb des Managementbereichs und ist ebenfalls eine direkte inhaltliche Übereinstimmung. INF.14.A6 verlangt zwar zunächst logische Trennung, ergänzt dies aber für gebäudeübergreifende GA-Kommunikation ausdrücklich um eine Separierung auf Netzeebene; damit stützt es den Aspekt der physischen bzw. netztechnischen Trennung zwischen Segmenten. Zusammen decken diese Anforderungen den wesentlichen Inhalt von ARCH.2.2.11 ab.
- **Lücken:** [gpt-5.4-mini] Keine wesentlichen Lücken, da die Kandidaten die physische Trennung von Netzsegmenten direkt abdecken. Die Regelung ist in einigen Kandidaten sektor- oder kontextbezogen (Management, GA), aber der zentrale Schutzbedarf der physischen Segmentierung ist enthalten.

### ARCH.2.2.8 — Segmentierung von Test und Betrieb
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `APP.4.4.A1` [Basis] Planung der Separierung der Anwendungen — _APP.4.4 Kubernetes_
  - `OPS.1.1.6.A13` [Standard] Trennung der Testumgebung von der Produktivumgebung — _OPS.1.1.6 Software-Tests und -Freigaben_
  - `SYS.1.7.A33` [Hoch] Trennung von Test- und Produktionssystemen unter z/OS — _SYS.1.7 IBM Z_
- **Begründung:** Gemittelte Kandidatenscores: APP.4.4.A1=0.47, OPS.1.1.6.A13=0.47, SYS.1.7.A33=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9500 gs_ids=OPS.1.1.6.A13;SYS.1.7.A33;APP.4.4.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung ARCH.2.2.8 verlangt, Verbindungen zwischen Testumgebungen und Betrieb einzuschränken bzw. eine saubere Trennung von Test- und Produktivumgebung sicherzustellen. OPS.1.1.6.A13 deckt dies direkt ab, da es ausdrücklich fordert, die Testumgebung von der Produktivumgebung getrennt zu betreiben. SYS.1.7.A33 entspricht inhaltlich ebenfalls dieser Trennung für z/OS-Umgebungen und adressiert zusätzlich technische Zugriffsmöglichkeiten über gemeinsame Festplatten und Parallel Sysplex. APP.4.4.A1 behandelt die Separierung von Test- und Produktions-Betriebsumgebungen in Kubernetes und verlangt dafür die Planung von Architekturen, Netzen und Separierungsmechanismen. Damit sind die wesentlichen Aspekte der GS++-Anforderung inhaltlich abgedeckt.
- **Lücken:** [gpt-5.4-mini] Keine wesentlichen Lücken; die Kandidaten decken die geforderte Trennung von Test und Betrieb auf allgemeiner bzw. plattformspezifischer Ebene ab.

### ARCH.2.2.9 — Segmentierung von IPv4 und IPv6
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A20` [Standard] Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A20=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9200 gs_ids=NET.1.1.A20
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.1.1.A20 passt inhaltlich am ehesten, da es die Zuordnung unterschiedlicher IPv4-/IPv6-Endgerätegruppen zu dedizierten Subnetzen fordert und damit eine Trennung bzw. Segmentierung nach Protokoll adressiert. Die GS++-Anforderung ARCH.2.2.9 verlangt jedoch allgemeiner, Verbindungen zwischen IPv4 und IPv6 in der Architektur einzuschränken. NET.1.1.A20 deckt die Segmentierung auf Subnetzebene ab, nicht aber zwingend alle Verbindungs- und Kommunikationsrestriktionen zwischen IPv4- und IPv6-Bereichen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind explizite Vorgaben zur Einschränkung von Verbindungen zwischen IPv4- und IPv6-Segmenten, z. B. über Firewall-/Routing-Regeln oder andere technische Kopplungsbeschränkungen. Die Anforderung beschreibt primär die getrennte Zuordnung zu Subnetzen, nicht die vollständige Verkehrsbegrenzung zwischen den Protokollwelten.

### ARCH.5.1.12 — Software-definierte Verbindungen
- **Confidence:** 0.41
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A2` [Basis] Festlegen der Firewall-Regeln — _NET.3.2 Firewall_
  - `NET.3.2.A27` [Hoch] Einsatz verschiedener Firewall-Betriebssysteme und -Produkte in einer mehrstufigen Firewall-Architektur — _NET.3.2 Firewall_
  - `OPS.1.2.5.A14` [Hoch] Dedizierte Clients und Konten bei der Fernwartung — _OPS.1.2.5 Fernwartung_
  - `OPS.1.2.5.A25` [Standard] Entkopplung der Kommunikation bei der Fernwartung — _OPS.1.2.5 Fernwartung_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A2=0.41, NET.3.2.A27=0.41, OPS.1.2.5.A14=0.41, OPS.1.2.5.A25=0.41
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8200 gs_ids=NET.3.2.A2;NET.3.2.A27;OPS.1.2.5.A25;OPS.1.2.5.A14
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A2 und NET.3.2.A27 passen insofern, als sie die netzseitige Steuerung von Kommunikationsverbindungen über fest definierte Firewall-Regeln bzw. eine mehrstufige Firewall-Architektur behandeln. OPS.1.2.5.A25 und OPS.1.2.5.A14 adressieren ebenfalls die Einschränkung von Verbindungen in Fernwartungsszenarien, insbesondere über Sprungserver und die Beschränkung auf vertrauenswürdige Systeme. Gemeinsam decken diese Anforderungen den Aspekt ab, dass Verbindungen technisch eingeschränkt und segmentiert werden können.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die wesentlichen GS++-spezifischen Kernelemente: die dynamische, kontextabhängige Bewertung von Verbindungen anhand aktueller Merkmale (z. B. device posture, Auslastung, Standort, Risikobewertung), software-definierte/logisch kontrollierte Netzwerkpfade sowie adaptive Policies/Mikrosegmentierung mit unveränderten Regeln und variabler Bewertung. Die Kandidaten beschreiben überwiegend statische Allowlist-/Firewall- oder Fernwartungsregeln und keine echte dynamische Kriteriensteuerung.

### ARCH.5.1.8 — Inspektion verschlüsselter Verbindungen
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A21` [Standard] Temporäre Entschlüsselung des Datenverkehrs — _NET.3.2 Firewall_
  - `NET.3.2.A28` [Hoch] Zentrale Filterung von aktiven Inhalten — _NET.3.2 Firewall_
  - `NET.1.1.A12` [Basis] Absicherung ausgehender interner Kommunikation zum Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A20` [Standard] Absicherung von grundlegenden Internetprotokollen — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A21=0.45, NET.3.2.A28=0.45, NET.1.1.A12=0.34, NET.3.2.A20=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9000 gs_ids=NET.3.2.A28;NET.3.2.A21
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6855 gs_ids=NET.3.2.A20;NET.1.1.A12
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A28 deckt die zentrale Filterung aktiver Inhalte über Sicherheitsproxies ab und nennt ausdrücklich auch die Entschlüsselung verschlüsselter Datenverkehre. NET.3.2.A21 deckt die temporäre Entschlüsselung verschlüsselter Verbindungen in nicht vertrauenswürdige Netze zur Protokollverifikation und Schadsoftwareprüfung ab. Beide Anforderungen passen damit inhaltlich zur Inspektion verschlüsselter Verbindungen. Die GS++-Anforderung ARCH.5.1.8 ist jedoch breiter formuliert: Sie verlangt eine Architektur für externe Netzanschlüsse, die den Inhalt unverschlüsselter und verschlüsselter Verbindungen abhängig von der Inhaltsart einschränken kann; das umfasst allgemeine Architektur- und Inhaltsrestriktion über die reine TLS-Entschlüsselung hinaus.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine Architekturvorgabe für externe Netzanschlüsse sowie die explizite, inhaltsartabhängige Einschränkung von unverschlüsseltem und verschlüsseltem Verkehr. Die Kandidaten behandeln primär Proxy-/Firewall-gestützte Entschlüsselung und Filterung, nicht die übergreifende Architekturgestaltung.

### ASST.2.1.1 — Informationsverantwortung
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `INF.13.A8` [Standard] Erstellung und Pflege eines Inventars für das TGM — _INF.13 Technisches Gebäudemanagement_
  - `ORP.1.A2` [Basis] Zuweisung der Zuständigkeiten — _ORP.1 Organisation_
- **Begründung:** Gemittelte Kandidatenscores: INF.13.A8=0.44, ORP.1.A2=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=ORP.1.A2;INF.13.A8
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.1.A2 passt inhaltlich, weil dort für Geschäftsprozesse, Anwendungen, IT-Systeme, Räume, Gebäude und Kommunikationsverbindungen festgelegt werden muss, wer zuständig ist; das trifft den Kern der geforderten Zuordnung von Zuständigkeiten. INF.13.A8 ergänzt dies für das technische Gebäudemanagement, da im Inventar Verantwortlichkeiten und Zuständigkeiten ersichtlich sein sollen. Beide Anforderungen adressieren jedoch primär die Zuordnung von Zuständigkeiten zu Prozessen/Systemen bzw. Inventareinträgen, nicht ausdrücklich das Ownership bzw. die institutionsinterne Zuständigkeit für Informationen und deren Verarbeitung als solche. Die spezifische Asset-Ownership von Informationen wird daher nicht vollständig abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die explizite Zuordnung der Zuständigkeit für konkrete Informationen und deren Verarbeitung (Information Asset Ownership), insbesondere die Möglichkeit, Informationen selbst oder nach Informations-Assets gruppiert zu verantworten. Die Kandidaten regeln vor allem Zuständigkeiten für Prozesse, Systeme und Inventare, nicht die informationsbezogene Verantwortlichkeit im engeren Sinn.

### ASST.2.2.1 — Aufdecken unautorisierter IT-Systeme
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.1.A6` [Standard] Durchführung des IT-Asset-Managements — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `OPS.3.2.A14` [Standard] Überwachung der Prozesse, Anwendungen und IT-Systeme — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.1.A6=0.46, OPS.3.2.A14=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9200 gs_ids=OPS.1.1.1.A6;OPS.3.2.A14
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.1.A6 passt inhaltlich, weil die Anforderung ein vollständiges, aktuelles Inventar aller IT-Assets verlangt und damit eine wichtige Grundlage zum Erkennen unbekannter bzw. nicht autorisierter Systeme schafft. OPS.3.2.A14 passt ebenfalls teilweise, da eine kontinuierliche Überwachung der eingesetzten Prozesse, Anwendungen und IT-Systeme das Aufdecken unbekannter oder nicht autorisierter IT-Systeme unterstützen kann. Beide Anforderungen decken jedoch nicht die eigentliche Zielsetzung der GS++-Anforderung vollständig ab, nämlich das gezielte aktive oder passive Erkennen unautorisierter Systeme im Netz sowie deren Behandlung (z. B. Quarantäne, Entfernung, Autorisierung).
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind insbesondere die konkreten Detektionsmethoden für unbekannte Systeme im Netz (z. B. aktive Netzscans, passive Traffic-Analyse, WLAN-Detektion) sowie die anschließenden Maßnahmen zur Behandlung gefundener Systeme. OPS.1.1.1.A6 adressiert primär Inventarisierung, nicht Erkennung im laufenden Netzbetrieb.

### ASST.4.4 — Nachweis des Zugangs
- **Confidence:** 0.35
- **Gemappte GS-Anforderungen:**
  - `DER.3.1.A27` [Standard] Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen — _DER.3.1 Audits und Revisionen_
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.3.2.A6` [Basis] Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: DER.3.1.A27=0.35, OPS.2.3.A7=0.35, OPS.3.2.A6=0.35
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7100 gs_ids=DER.3.1.A27;OPS.3.2.A6;OPS.2.3.A7
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.3.1.A27 adressiert die nachvollziehbare und revisionssichere Aufbewahrung von Unterlagen zu Audits und Revisionen und trifft damit den Aspekt der dokumentierten, archivierten Nachweisführung teilweise. OPS.3.2.A6 und OPS.2.3.A7 regeln bei der Beendigung von Outsourcing-Verhältnissen die Rückgabe von Informationen sowie die Dokumentation der Rückgabe und die Prüfung der Rechtesituation. Diese Anforderungen haben jedoch keinen eigentlichen Bezug zum Nachweis des Zugangs einer Nachricht an einen Empfänger. Der Kern der GS++-Anforderung ASST.4.4 ist der manipulationssichere Zugangsnachweis für übermittelte Nachrichten, inklusive Zeitpunkt, Empfänger und ggf. inhaltlicher Belege; genau diese spezifische Kommunikations- bzw. Empfangsbestätigung wird durch die Kandidaten nicht vollständig abgebildet.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die eigentliche Empfangsbestätigung bzw. der manipulationssichere Nachweis, dass eine konkrete Nachricht einen bestimmten Empfänger erreicht hat, einschließlich nachvollziehbarer Protokollierung von Versand-/Zieladressen, Zeitpunkt und ggf. Nachrichteninhalten. Die Kandidaten behandeln eher Archivierung, Revision und Outsourcing-Rückgabe als den Zugangsnachweis im Kommunikationsprozess.

### ASST.6.1 — Abhandenkommen
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `DER.2.1.A7` [Standard] Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `SYS.3.1.A12` [Standard] Verlustmeldung für Laptops — _SYS.3.1 Laptops_
  - `SYS.3.3.A2` [Basis] Sperrmaßnahmen bei Verlust eines Mobiltelefons — _SYS.3.3 Mobiltelefon_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.1.A7=0.44, SYS.3.1.A12=0.44, SYS.3.3.A2=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=SYS.3.1.A12;DER.2.1.A7;SYS.3.3.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] SYS.3.1.A12 deckt die konkrete Verlust- bzw. Diebstahlmeldung für Laptops ab, einschließlich Meldewege und Umgang mit wieder auftauchenden Geräten. SYS.3.3.A2 deckt die Sofortmaßnahmen bei Verlust eines Mobiltelefons ab, insbesondere SIM-Sperrung sowie Fernlöschung/-sperrung. DER.2.1.A7 deckt die übergreifende organisatorische Anforderung ab, eine Vorgehensweise zur Behandlung von Sicherheitsvorfällen zu definieren und dokumentiert vorzuhalten. Zusammen ergeben die drei Anforderungen eine inhaltliche Teilabdeckung des Themas "Abhandenkommen von Assets".
- **Lücken:** [gpt-5.4-mini] Die GS++-Anforderung verlangt eine allgemeine, assetübergreifende Vorgehensweise für verlorene/gestohlene/außer Kontrolle geratene Assets. Abgedeckt sind nur Teilaspekte für Laptops und Mobiltelefone sowie die generische Incident-Response-Organisation. Nicht ausreichend abgedeckt sind insbesondere assetunabhängige Maßnahmen für beliebige Informationswerte und physische Assets, das strukturierte Vorgehen nach Eintritt des Verlustereignisses für alle Asset-Arten, sowie beispielhafte Inhalte wie Fundbüro/Ermittlungsbehörden, Sperrung weiterer Authentisierungsmittel oder datenschutzbezogene Sofortmaßnahmen im Allgemeinen.

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
[gpt-5.4-mini] coverage=teilweise confidence=0.9100 gs_ids=APP.6.A13;SYS.2.1.A16;SYS.1.9.A15;SYS.3.2.2.A7;SYS.4.4.A13
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Anforderungen APP.6.A13, SYS.2.1.A16, SYS.1.9.A15, SYS.3.2.2.A7 und SYS.4.4.A13 decken den Kernaspekt der Deinstallation bzw. Entfernung nicht mehr benötigter Anwendungen und Komponenten ab. APP.6.A13 fordert bei einer Deinstallation das Entfernen nicht mehr benötigter Dateien und das Rückgängigmachen von Systemeinträgen. SYS.2.1.A16 verlangt auf Clients die Deaktivierung oder Deinstallation nicht benötigter Programme, Dienste und auch Kennungen sowie die Verhinderung einer Reaktivierung. SYS.1.9.A15 fordert auf Terminalservern das Entfernen nicht benötigter Anwendungen oder alternativ die Unterbindung ihrer Ausführung. SYS.3.2.2.A7 beschreibt die Deinstallation von Apps per MDM, einschließlich erzwungener Deinstallation. SYS.4.4.A13 behandelt auf IoT-Geräten das Deaktivieren oder Deinstallieren nicht benötigter Protokolle, Dienste, Anmeldekennungen und Schnittstellen. Damit ist die eigentliche Entfernung nicht benötigter Software-/Anwendungskomponenten abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die explizit geforderten organisatorischen und inhaltlichen Ergänzungen der GS++-Anforderung: geregelter Prozess mit nachvollziehbarer Dokumentation, Umgang mit zugehörigen Konfigurationen, temporären Daten und Berechtigungen, sowie der Cloud-spezifische Fall, dass Daten zu löschen sind, wenn die Anwendungsinstanz nicht unter Kontrolle der Institution steht. Die Kandidaten behandeln überwiegend technische Deinstallation, aber nicht durchgängig die komplette Berechtigungs- und Datenbereinigung über alle Umgebungen hinweg.

### ASST.7.6 — Autorisierung von Veräußerungen
- **Confidence:** 0.34
- **Gemappte GS-Anforderungen:**
  - `CON.6.A1` [Basis] Regelung für die Löschung und Vernichtung von Informationen — _CON.6 Löschen und Vernichten_
  - `CON.6.A2` [Basis] Ordnungsgemäßes Löschen und Vernichten von schützenswerten Betriebsmitteln und Informationen — _CON.6 Löschen und Vernichten_
  - `CON.6.A8` [Standard] Erstellung einer Richtlinie für die Löschung und Vernichtung von Informationen — _CON.6 Löschen und Vernichten_
  - `OPS.1.1.6.A4` [Basis] Freigabe der Software — _OPS.1.1.6 Software-Tests und -Freigaben_
  - `OPS.2.3.A10` [Standard] Etablierung einer zuständigen Person für das Auslagerungsmanagement — _OPS.2.3 Nutzung von Outsourcing_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `SYS.3.1.A7` [Standard] Geregelte Übergabe und Rücknahme eines Laptops — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: CON.6.A1=0.34, CON.6.A2=0.34, CON.6.A8=0.34, OPS.1.1.6.A4=0.34, OPS.2.3.A10=0.34, ORP.5.A4=0.34, SYS.3.1.A7=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.6700 gs_ids=CON.6.A2;SYS.3.1.A7;CON.6.A1;CON.6.A8;OPS.1.1.6.A4;ORP.5.A4;OPS.2.3.A10
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.6.A2 und SYS.3.1.A7 decken den Teilaspekt ab, dass vor der Veräußerung schutzbedürftige Informationen bzw. Datenträger sicher gelöscht oder vernichtet werden müssen; CON.6.A1 und CON.6.A8 regeln dies organisatorisch über Prozess und Richtlinie für Löschen/Vernichten. OPS.1.1.6.A4 passt nur insoweit, als eine dokumentierte Freigabe nach Prüfung rechtlicher und organisatorischer Vorgaben gefordert wird, was dem Autorisierungsgedanken ähnelt, aber auf Software-Freigaben beschränkt ist. ORP.5.A4 deckt den Umgang mit rechtlichen, vertraglichen und sonstigen Vorgaben ab, was bei Veräußerungen relevant sein kann, ersetzt aber keine explizite Veräußerungsautorisierung. OPS.2.3.A10 betrifft die Einbindung einer zuständigen Person in Vertragsgestaltung und Auslagerungsmanagement; das ist nur randnah zum geordneten Übergang an Dritte und daher höchstens sehr indirekt passend. Insgesamt fehlt in allen Kandidaten die eigentliche Kernforderung, nämlich eine explizite, vor der endgültigen Abgabe greifende Autorisierung von Veräußerungen von Assets nach Schutzbedarf, Asset-Owner und Freigabetiefe.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt ist die explizite Autorisierung von Veräußerungen als eigener Freigabeprozess vor Eigentums-/Besitzübergang, einschließlich der Steuerung nach Schutzbedarf (z. B. unterschiedliche Genehmigungstiefen), der Festlegung von Rollen wie Asset-Owner und Informationssicherheitsbeauftragte/r sowie der spezifischen Freigabelogik für Verkauf, Spende, Leasingrückgabe oder Recycling. Die Kandidaten behandeln vor allem Löschung/Vernichtung, allgemeine Freigaben oder Compliance, aber nicht die formale Veräußerungsgenehmigung selbst.

### BER.1.1.3 — Bekanntgabe
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `APP.5.4.A5` [Basis] Rollen- und Berechtigungskonzept für UCC — _APP.5.4 Unified Communications und Collaboration (UCC)_
  - `CON.8.A1` [Standard] Definition von Rollen und Zuständigkeiten — _CON.8 Software-Entwicklung_
  - `OPS.1.1.3.A11` [Standard] Kontinuierliche Dokumentation der Informationsverarbeitung — _OPS.1.1.3 Patch- und Änderungsmanagement_
  - `OPS.1.2.5.A6` [Standard] Erstellung einer Richtlinie für die Fernwartung — _OPS.1.2.5 Fernwartung_
- **Begründung:** Gemittelte Kandidatenscores: APP.5.4.A5=0.43, CON.8.A1=0.43, OPS.1.1.3.A11=0.43, OPS.1.2.5.A6=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=OPS.1.2.5.A6;OPS.1.1.3.A11;CON.8.A1;APP.5.4.A5
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.2.5.A6 passt inhaltlich, weil dort explizit gefordert wird, eine Richtlinie zu erstellen, die allen Zuständigen bekannt sein soll. OPS.1.1.3.A11 passt teilweise, weil Änderungen dokumentiert und dazu Regelungen erarbeitet werden sollen, was die Bekanntgabe von Verfahren und Regelungen unterstützt. CON.8.A1 passt teilweise, da Rollen und Zuständigkeiten festzulegen sind, was eine Voraussetzung dafür ist, die richtigen Personen zu informieren. APP.5.4.A5 passt ebenfalls teilweise, weil Rollen- und Berechtigungskonzepte festgehalten, geprüft und aktualisiert werden müssen; das deckt aber nicht die explizite Pflicht zur aktiven Information der zuständigen Personen über Verfahren und Regelungen vollständig ab.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die explizite Verteilungs- und Benachrichtigungspflicht gegenüber den zuständigen Personen oder Rollen sowie der konkrete Fokus auf Bekanntgabe im Onboarding und bei Änderungen per automatischer Benachrichtigung. Die Kandidaten regeln Dokumentation, Festlegung und Bekanntheit von Richtlinien eher indirekt, aber nicht die gezielte und laufende Information aller Betroffenen.

### BER.1.2 — Regelmäßige Überprüfung
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `DER.1.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `DER.1.A13` [Standard] Regelmäßige Audits der Detektionssysteme — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `DER.4.A14` [Hoch] Regelmäßige Überprüfung und Verbesserung der Notfallmaßnahmen — _DER.4 Notfallmanagement_
  - `INF.1.A36` [Standard] Regelmäßige Aktualisierungen der Dokumentation — _INF.1 Allgemeines Gebäude_
  - `OPS.1.1.1.A2` [Basis] Festlegung von Rollen und Berechtigungen für den IT-Betrieb — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `OPS.1.2.2.A2` [Basis] Entwicklung eines Archivierungskonzepts — _OPS.1.2.2 Archivierung_
  - `ORP.5.A8` [Standard] Regelmäßige Überprüfungen des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `APP.4.3.A20` [Standard] Regelmäßige Audits — _APP.4.3 Relationale Datenbanken_
  - `OPS.1.2.2.A13` [Standard] Regelmäßige Revision der Archivierungsprozesse — _OPS.1.2.2 Archivierung_
- **Begründung:** Gemittelte Kandidatenscores: DER.1.A1=0.45, DER.1.A13=0.45, DER.4.A14=0.45, INF.1.A36=0.45, OPS.1.1.1.A2=0.45, OPS.1.2.2.A2=0.45, ORP.5.A8=0.45, APP.4.3.A20=0.33, OPS.1.2.2.A13=0.33
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=ORP.5.A8;DER.4.A14;DER.1.A13;DER.1.A1;OPS.1.1.1.A2;INF.1.A36;OPS.1.2.2.A2
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6600 gs_ids=APP.4.3.A20;OPS.1.2.2.A13
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung BER.1.2 fordert die regelmäßige sowie anlassbezogene Überprüfung von Verfahren und Regelungen auf Aktualität. Inhaltlich passen dazu ORP.5.A8, da dort ein Verfahren zur regelmäßigen Überprüfung von Compliance-Management und den daraus resultierenden Anforderungen und Maßnahmen auf Effizienz und Effektivität verlangt wird; DER.4.A14, weil Notfallmaßnahmen regelmäßig oder bei größeren Änderungen überprüft werden sollen; DER.1.A13, weil Detektionssysteme regelmäßig auditiert und auf Aktualität und Wirksamkeit geprüft werden sollen; DER.1.A1, weil die spezifische Sicherheitsrichtlinie regelmäßig auf korrekte Umsetzung überprüft werden muss; OPS.1.1.1.A2, weil Rollen und Berechtigungen regelmäßig geprüft und an aktuelle Gegebenheiten angepasst werden müssen; INF.1.A36, weil Dokumentationen regelmäßig auf Aktualität geprüft werden sollen; sowie OPS.1.2.2.A2, weil das Archivierungskonzept regelmäßig an aktuelle Gegebenheiten anzupassen ist. Diese Anforderungen treffen den Kern 'regelmäßige Überprüfung/Aktualisierung von Regelungen und Verfahren', aber sie sind jeweils domänenspezifisch und decken nicht allgemein alle Arten von Verfahren und Regelungen ab, die BER.1.2 offen formuliert verlangt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die generische, bereichsübergreifende Pflicht zur regelmäßigen und anlassbezogenen Überprüfung aller relevanten Verfahren und Regelungen der Berechtigung. Die Kandidaten beziehen sich nur auf einzelne Teilbereiche (z. B. Notfallmanagement, Compliance, Rollen/Berechtigungen, Dokumentation, Archivierung) und nennen nicht durchgängig die anlassbezogene Überprüfung bei Ereignissen wie Sicherheitsvorfällen, strategischen Änderungen oder neuen gesetzlichen Anforderungen. Ebenso fehlt eine explizite allgemeine Regelung zur Überprüfung von Verfahren und Regelungen im Berechtigungsmanagement als solchem.

### BER.2.5 — Deaktivierung bei Weggang
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.3.2.A6` [Basis] Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.3.2 Anbieten von Outsourcing_
  - `ORP.2.A2` [Basis] Geregelte Verfahrensweise beim Weggang von Mitarbeitenden — _ORP.2 Personal_
- **Begründung:** Gemittelte Kandidatenscores: OPS.2.3.A7=0.44, OPS.3.2.A6=0.44, ORP.2.A2=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=OPS.2.3.A7;OPS.3.2.A6;ORP.2.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.2.3.A7 und OPS.3.2.A6 behandeln die Beendigung von Outsourcing-Verhältnissen und das Aufheben von Zugangs- bzw. Zugriffsrechten nach Vertragsende. ORP.2.A2 regelt beim Weggang von Mitarbeitenden das Einziehen von Ausweisen und Zutrittsberechtigungen sowie die Information betroffener Stellen. Gemeinsam treffen die Kandidaten den organisatorischen Kern der Entziehung von Berechtigungen bei Weggang, aber die GS++-Anforderung BER.2.5 ist enger und fordert ausdrücklich die Deaktivierung der zugeordneten Identität der Nutzenden bei Weggang (oder deren Löschung) im Identitätsmanagement. Diese explizite technische Konten-/Identitätsdeaktivierung wird durch die Kandidaten nicht vollständig abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt ist die explizite Deaktivierung oder Löschung der Identität bzw. des Benutzerkontos im Identitätsmanagement bei dauerhaftem Weggang. Die Kandidaten adressieren vor allem organisatorische Maßnahmen und das Aufheben von Zugangs-/Zutritts-/Zugriffsrechten, jedoch nicht die konkrete Deaktivierung der zugeordneten Identität.

### BER.3.15 — Keine Gruppenkonten
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.2.A22` [Basis] Trennung von administrativen und anderen Tätigkeiten — _OPS.1.1.2 Ordnungsgemäße IT-Administration_
  - `SYS.2.4.A3` [Basis] Verwendung geeigneter Konten — _SYS.2.4 Clients unter macOS_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.2.A22=0.43, SYS.2.4.A3=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=SYS.2.4.A3;OPS.1.1.2.A22
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] SYS.2.4.A3 fordert für macOS bei Mehrbenutzung jeweils ein eigenes Konto pro Benutzendem und damit die Trennung von Personen auf Kontenebene. OPS.1.1.2.A22 verlangt außerdem, dass Zugangskennungen für IT-Administration sich von Kennungen in anderem Kontext unterscheiden und dass dieselbe Instanz nicht für andere Aufgaben verwendet wird. Beide Anforderungen zielen auf saubere Kontentrennung und gegen gemeinsame Nutzung von Zugangskonten. Die GS++-Anforderung BER.3.15 geht jedoch spezifisch weiter, indem sie Gruppenkonten generell untersagen soll; dieses explizite Verbot wird durch die Kandidaten nicht vollständig abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist das explizite generelle Verbot von Gruppenkonten bzw. gemeinsam genutzten Zugangskonten als organisatorische Berechtigungsregel. SYS.2.4.A3 deckt nur den Mehrbenutzerfall auf macOS mit separaten Benutzerkonten ab, OPS.1.1.2.A22 primär die Trennung administrativer und nicht-administrativer Kennungen. Ein allgemeines Verbot von Gruppenkonten für alle Kontexte fehlt.

### BER.7.16.3 — Erneuerung
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `CON.1.A4` [Basis] Geeignetes Schlüsselmanagement — _CON.1 Kryptokonzept_
  - `CON.1.A5` [Standard] Sicheres Löschen und Vernichten von kryptografischen Schlüsseln — _CON.1 Kryptokonzept_
  - `DER.2.3.A4` [Basis] Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln — _DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle_
- **Begründung:** Gemittelte Kandidatenscores: CON.1.A4=0.45, CON.1.A5=0.45, DER.2.3.A4=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=CON.1.A4;DER.2.3.A4;CON.1.A5
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.1.A4 passt teilweise, weil dort festgelegt wird, wie mit Schlüsseln und Zertifikaten umzugehen ist und dass die Integrität und Authentizität öffentlicher Schlüssel sichergestellt sein muss; außerdem sollen zeitlich begrenzte Zertifikate rechtzeitig erneuert werden. DER.2.3.A4 passt für den Sonderfall kompromittierter Schlüssel bzw. CA, da dort die Neuerzeugung, Sperrung und der Rückruf kompromittierter Schlüssel und Zertifikate gefordert werden. CON.1.A5 ergänzt dies insofern, als nicht mehr benötigte private Schlüssel sicher gelöscht oder vernichtet werden sollen. Gemeinsam decken die Kandidaten aber nicht den spezifischen Prüfakt bei der Erneuerung einer Beglaubigung ab, insbesondere nicht die explizite Verifikation des Schlüssels anhand von Vorgaben für die Schlüsselbeglaubigung (z. B. Signaturprüfung, Fingerprint-Abgleich, Transparenzlog), sondern nur allgemeines Schlüsselmanagement, Erneuerung und Reaktion auf Kompromittierung.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkrete Prüfung des Schlüssels bei Zertifikatserneuerung, die formalen Vorgaben für die Schlüsselbeglaubigung im Erneuerungsprozess sowie die geforderte Validierung gegen Sperrlisten/Transparenzregister als spezifischer Bestandteil dieser Anforderung.

### BER.7.16.6 — Revocationstatus
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `DER.2.3.A4` [Basis] Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln — _DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.3.A4=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9700 gs_ids=DER.2.3.A4
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.2.3.A4 deckt die wesentliche inhaltliche Anforderung ab, kompromittierte kryptografische Schlüssel und Zertifikate zuverlässig zu sperren und zurückzurufen. Das entspricht dem geforderten Dokumentieren des Revocationstatus eines Schlüssels im Verzeichnis öffentlicher Schlüssel, da der Status den Rückzug bzw. die Sperrung eines Schlüssels abbildet. Die technische und organisatorische Zielrichtung ist damit inhaltlich gleichgerichtet.

## Keine Abdeckung (1)

### BER.6.8 — Kriterien für die Qualität von Passwörtern
- **Confidence:** 0.48
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9700 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidatenanforderungen deckt die GS++-Anforderung BER.6.8 inhaltlich ab. BER.6.8 verlangt Kriterien zur Qualität von Passwörtern selbst, insbesondere abhängig von Lebensdauer, Angriffsmöglichkeiten, Passwortlänge/Entropie und ggf. Mehr-Faktor-Authentisierung bzw. maximalen Fehlversuchen. Die Kandidaten behandeln dagegen andere Themen: z. B. ORP.4.A21, CON.10.A16, SYS.2.1.A37 und OPS.1.2.5.A17 regeln Mehr-Faktor-Authentisierung, aber nicht Passwortqualitätskriterien; ORP.4.A11 regelt das Zurücksetzen von Passwörtern; CON.1.A9 und CON.1.A10 betreffen Kryptokonzept/Kriterien für kryptografische Funktionen; SYS.2.3.A9 behandelt die sichere Übergabe von Passwörtern auf der Kommandozeile. Somit liegt keine echte inhaltliche Übereinstimmung vor.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die Festlegung von Passwortqualitätskriterien wie Mindestlänge, Entropie, Zeichensätze, differenzierte Kriterien nach Lebensdauer und Angriffsszenario sowie die Verknüpfung dieser Kriterien mit konkreten Schutzmaßnahmen wie maximale Passwortversuche oder MFA.
