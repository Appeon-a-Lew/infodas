# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:54:59

**Gesamt:** 20 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 20 |
| Keine Abdeckung | 0 |

## Teilweise abgedeckt (20)

### ARCH.1.1.1 — Dokumentation
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `APP.6.A10` [Standard] Erstellung einer Sicherheitsrichtlinie für den Einsatz der Software — _APP.6 Allgemeine Software_
  - `APP.7.A6` [Standard] Dokumentation der Anforderungen an die Individualsoftware — _APP.7 Entwicklung von Individualsoftware_
  - `CON.8.A12` [Standard] Ausführliche Dokumentation — _CON.8 Software-Entwicklung_
  - `DER.3.1.A6` [Standard] Definition der Prüfungsgrundlage und eines einheitlichen Bewertungsschemas — _DER.3.1 Audits und Revisionen_
  - `IND.1.A11` [Standard] Sichere Beschaffung und Systementwicklung — _IND.1 Prozessleit- und Automatisierungstechnik_
  - `NET.1.2.A12` [Standard] Ist-Aufnahme und Dokumentation des Netzmanagements — _NET.1.2 Netzmanagement_
  - `SYS.1.1.A11` [Standard] Festlegung einer Sicherheitsrichtlinie für Server — _SYS.1.1 Allgemeiner Server_
  - `SYS.4.4.A6` [Standard] Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.6.A10=0.43, APP.7.A6=0.43, CON.8.A12=0.43, DER.3.1.A6=0.43, IND.1.A11=0.43, NET.1.2.A12=0.43, SYS.1.1.A11=0.43, SYS.4.4.A6=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=APP.6.A10;CON.8.A12;DER.3.1.A6;NET.1.2.A12;IND.1.A11;APP.7.A6;SYS.1.1.A11;SYS.4.4.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung ARCH.1.1.1 verlangt allgemein, dass Verfahren und Regelungen dokumentiert werden. Das wird inhaltlich durch mehrere Kandidaten teilweise getroffen: APP.6.A10 fordert die Zusammenfassung von Regelungen in einer Sicherheitsrichtlinie; CON.8.A12 verlangt ausreichende Projekt-, Funktions- und Schnittstellendokumentationen; DER.3.1.A6 verlangt eine dokumentierte einheitliche Prüfungsgrundlage und ein Bewertungsschema; NET.1.2.A12 fordert eine vollständige und aktuelle Dokumentation des Netzmanagements; IND.1.A11 verlangt die Dokumentation von Regelungen zur Informationssicherheit bei Beschaffung/Planung/Entwicklung; APP.7.A6 fordert die umfassende Dokumentation von Anforderungen und Sicherheitsprofilen; SYS.1.1.A11 und SYS.4.4.A6 verlangen jeweils eine Sicherheitsrichtlinie mit dokumentierter Umsetzung bzw. Ergebnisdokumentation. Alle diese Anforderungen zeigen den Dokumentationsgedanken für Regelungen und Verfahren, jedoch jeweils nur bezogen auf ihren spezifischen Fachkontext.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind der ausdrücklich allgemeine, bausteinübergreifende Charakter der GS++-Anforderung sowie die Möglichkeit, die Dokumentation zielgruppengerecht und in beliebiger organisatorischer Form (eigenständiges Dokument, Abschnitt, digitales Managementsystem) zu strukturieren. Einige Kandidaten dokumentieren nur fachliche Teilbereiche (z. B. Webanwendung, Server, IoT, Netzmanagement, Audits) statt die allgemeinen Architektur-Verfahren und -Regelungen insgesamt.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.78
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A11` [Basis] Absicherung eingehender Kommunikation vom Internet in das interne Netz — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.3.A11` [Standard] Sichere Anbindung eines externen Netzes — _NET.3.3 VPN_
  - `CON.7.A7` [Basis] Sicherer Remote-Zugriff auf das Netz der Institution — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `CON.7.A8` [Basis] Sichere Nutzung von öffentlichen WLANs — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `INF.10.A6` [Standard] Einrichtung sicherer Netzzugänge — _INF.10 Besprechungs-, Veranstaltungs- und Schulungsräume_
  - `NET.1.1.A10` [Basis] DMZ-Segmentierung für Zugriffe aus dem Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A18` [Standard] P-A-P-Struktur für die Internet-Anbindung — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `SYS.3.1.A8` [Standard] Sicherer Anschluss von Laptops an Datennetze — _SYS.3.1 Laptops_
  - `SYS.3.1.A9` [Basis] Sicherer Fernzugriff mit Laptops — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A11=0.78, NET.3.3.A11=0.78, CON.7.A7=0.42, CON.7.A8=0.42, INF.10.A6=0.42, NET.1.1.A10=0.42, NET.1.1.A18=0.42, NET.1.1.A4=0.42, SYS.3.1.A8=0.42, SYS.3.1.A9=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=NET.1.1.A4;NET.1.1.A10;NET.1.1.A18;NET.1.1.A11;NET.3.3.A11;SYS.3.1.A9;CON.7.A7;CON.7.A8;SYS.3.1.A8;INF.10.A6
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung ARCH.2.2.1 zielt darauf ab, externe Netzanschlüsse in der Architektur zu begrenzen, um Angriffsfläche, unerwünschte Ein-/Ausleitungen und Datenabfluss zu reduzieren. Inhaltlich passen dazu insbesondere NET.1.1.A4, NET.1.1.A10, NET.1.1.A18, NET.1.1.A11 und NET.1.1.A9? Nein: aus der Kandidatenliste ist NET.1.1.A9 nur die allgemeine Einstufung nicht vertrauenswürdiger Netze und unterstützt die Abgrenzung, aber sie regelt keine konkrete Einschränkung von externen Anschlüssen. Stärker decken NET.1.1.A4, NET.1.1.A10, NET.1.1.A18 und NET.1.1.A11 die technische Begrenzung externer Anbindungen, DMZ-Trennung und den zwingenden sicheren Kanal für Zugriffe aus dem Internet ab. NET.3.3.A11 ergänzt, dass VPN-Verbindungen nur zwischen vorgesehenen Systemen aufgebaut werden sollen, also externe Anbindungen kontrolliert werden. Für mobile Systeme und Fernzugriff sind SYS.3.1.A9, CON.7.A7 und CON.7.A8 relevant, weil sie den Zugriff aus öffentlichen Netzen bzw. WLANs nur über einen sicheren Kommunikationskanal/VPN zulassen. SYS.3.1.A8 und INF.10.A6 passen ebenfalls teilweise, weil sie den sicheren Anschluss von Laptops sowie die Trennung bzw. Absicherung von Netzzugängen in Räumen mit externen Geräten adressieren. Dennoch bleibt die GS++-Anforderung allgemeiner und architektonischer: Sie fordert das einschränkende Design externer Netzanschlüsse als Grundsatz, während die Kandidaten überwiegend konkrete Teilfälle wie Internetzugang, VPN, WLAN, DMZ oder mobile Endgeräte regeln. Eine vollständige Abdeckung liegt daher nicht vor.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind der allgemeine, architekturweite Grundsatz zur Einschränkung externer Netzanschlüsse sowie die explizite Zielsetzung, unerwünschte Ein- und Ausleitungen und Datenabflüsse in allen Segmenten systematisch zu minimieren. Die Kandidaten behandeln vor allem konkrete Umsetzungen (Internet/VPN, DMZ, mobile Systeme, WLAN, Besprechungsräume), nicht aber eine durchgängig allgemeine Architekturregel für alle externen Netzanschlüsse.

### ARCH.2.2.11 — Physische Segmentierung
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.4.2.A4` [Basis] Einschränkung der Erreichbarkeit über VoIP — _NET.4.2 VoIP_
  - `OPS.1.1.2.A16` [Standard] Erweiterte Sicherheitsmaßnahmen für Administrationszugänge — _OPS.1.1.2 Ordnungsgemäße IT-Administration_
  - `SYS.1.5.A4` [Basis] Sichere Konfiguration eines Netzes für virtuelle Infrastrukturen — _SYS.1.5 Virtualisierung_
  - `SYS.1.8.A15` [Standard] Sichere Trennung von Mandanten in Speicherlösungen — _SYS.1.8 Speicherlösungen_
  - `NET.1.1.A22` [Standard] Spezifikation des Segmentierungskonzepts — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A23` [Standard] Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A31` _(nicht im Korpus gefunden)_
  - `NET.1.1.A33` _(nicht im Korpus gefunden)_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.43, NET.1.1.A4=0.43, NET.4.2.A4=0.43, OPS.1.1.2.A16=0.43, SYS.1.5.A4=0.43, SYS.1.8.A15=0.43, NET.1.1.A22=0.34, NET.1.1.A23=0.34, NET.1.1.A31=0.34, NET.1.1.A33=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=NET.1.1.A4;SYS.1.5.A4;INF.14.A6;SYS.1.8.A15;OPS.1.1.2.A16;NET.4.2.A4
[manual:gspp_compliance_v3approach] coverage=teilweise confidence=0.6711 gs_ids=NET.1.1.A31;NET.1.1.A23;NET.1.1.A33;NET.1.1.A22
Model-Begründungen:
[gpt-5.4-mini] NET.1.1.A4 passt, weil dort Netze/Zonen ausdrücklich physisch zu separieren sind und die Trennung durch Firewalls ergänzt wird. Das deckt den Kern der physischen Segmentierung auf Netzebene ab, allerdings nur bezogen auf interne/DMZ-/Außenanbindungen und nicht allgemein als Architekturprinzip. SYS.1.5.A4 und SYS.1.8.A15 adressieren ebenfalls das Verhindern der Umgehung von Sicherheitsmechanismen bzw. die sichere Trennung in virtualisierten Umgebungen, was den Sicherheitsgedanken der Anforderung stützt, aber primär virtuelle statt physische Segmentierung betrifft. INF.14.A6 fordert eine mindestens logische Trennung von GA-Netzen und kontrollierte Kommunikation, ggf. auch netztechnische Separierung; das ist thematisch nah, aber nicht spezifisch physische Segmentierung allgemein. OPS.1.1.2.A16 fordert die Trennung von Administrationsnetzen und produktiven Netzen durch Filter- und Segmentierungsmaßnahmen; das ist eine konkrete Segmentierungsmaßnahme, aber nur für Adminzugänge. NET.4.2.A4 verhindert direkte Verbindungen aus unsicheren Netzen zu VoIP-Komponenten und setzt damit ebenfalls auf kontrollierte, getrennte Zugänge, jedoch nur im VoIP-Kontext.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die generelle Anforderung, Netze architektonisch physisch voneinander zu trennen, statt nur logisch oder über technische Kontrollmechanismen zu segmentieren. Die Kandidaten behandeln überwiegend spezielle Anwendungsdomänen (Virtualisierung, GA, Admin-, VoIP- oder Mandantentrennung) und nicht die allgemeine, domänenübergreifende physische Segmentierung aller relevanten Netze. Auch die explizite Aussage, dass physische Trennung Konfigurationsfehler und Umgehungen besonders wirksam reduziert, wird nur indirekt gestützt, nicht als allgemeine Architekturvorgabe umgesetzt.

### ARCH.2.2.8 — Segmentierung von Test und Betrieb
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.6.A13` [Standard] Trennung der Testumgebung von der Produktivumgebung — _OPS.1.1.6 Software-Tests und -Freigaben_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.6.A13=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9600 gs_ids=OPS.1.1.6.A13
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.6.A13 deckt die Kernforderung direkt ab: Es fordert ausdrücklich, dass Software nur in einer vorgesehenen Testumgebung getestet wird und dass diese Testumgebung von der Produktivumgebung getrennt betrieben werden SOLL. Damit entspricht es inhaltlich der geforderten Segmentierung bzw. Einschränkung von Verbindungen zwischen Test und Betrieb. Die weiteren Aspekte der Grundschutz++-Anforderung (saubere Trennung zur Vermeidung von Übergriffen und Ressourcenkonflikten) sind vom Trennungsgebot ebenfalls erfasst.
- **Lücken:** [gpt-5.4-mini] Keine wesentlichen Lücken; die Anforderung ist etwas allgemeiner formuliert als die GS++-Anforderung, trifft aber den Schutzaspekt vollständig.

### ARCH.2.2.9 — Segmentierung von IPv4 und IPv6
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A20` [Standard] Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A20=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=NET.1.1.A20
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.1.1.A20 passt inhaltlich am besten, weil es die Zuordnung unterschiedlicher IPv4-/IPv6-Endgerätegruppen zu dedizierten Subnetzen verlangt und damit eine technische Segmentierung nach IP-Protokoll beschreibt. Das geht in die gleiche Richtung wie die GS++-Anforderung ARCH.2.2.9, die Verbindungen zwischen IPv4 und IPv6 einschränken will. Allerdings beschreibt NET.1.1.A20 primär die Subnetz-Zuordnung von Endgeräten und nicht ausdrücklich die allgemeine Einschränkung von Verbindungen zwischen IPv4- und IPv6-Segmenten bzw. zwischen Protokollwelten in der gesamten Netzarchitektur.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine Vorgabe zur Einschränkung von Verbindungen zwischen IPv4 und IPv6 sowie die explizite Betrachtung der Wechselwirkungen/Sicherheitsunterschiede beider Protokollstacks. Die Anforderung adressiert eher die Segmentierungsmaßnahme über dedizierte Subnetze als die umfassende Protokolltrennung.

### ARCH.5.1.12 — Software-definierte Verbindungen
- **Confidence:** 0.41
- **Gemappte GS-Anforderungen:**
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.3.2.A2` [Basis] Festlegen der Firewall-Regeln — _NET.3.2 Firewall_
  - `NET.3.3.A11` [Standard] Sichere Anbindung eines externen Netzes — _NET.3.3 VPN_
  - `NET.3.4.A6` [Standard] Festlegung von Notfallprozessen für NAC — _NET.3.4 Network Access Control_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.41, NET.3.2.A2=0.41, NET.3.3.A11=0.41, NET.3.4.A6=0.41
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8300 gs_ids=NET.3.2.A2;INF.14.A6;NET.3.4.A6;NET.3.3.A11
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A2 passt inhaltlich, weil dort Kommunikationsverbindungen per Firewall-Filterregeln festgelegt und unerlaubte Verbindungen unterbunden werden; das ist eine technische Einschränkung von Verbindungen, allerdings statisch regelbasiert. INF.14.A6 deckt die kontrollierte und reglementierte Kommunikation zwischen logisch getrennten Netzen ab und verlangt an den Übergängen Sicherheitsfunktionen wie Firewalls; auch hier wird die Verbindungsbegrenzung adressiert, aber nicht dynamisch. NET.3.3.A11 ist einschlägig, weil VPN-Verbindungen nur zwischen vorgesehenen IT-Systemen und Diensten aufgebaut werden sollen; dies begrenzt Verbindungen auf definierte Endpunkte, jedoch ohne dynamische Kriterien. NET.3.4.A6 hat nur einen engen Teilbezug, da NAC-Notfallprozesse die zeitweise Deaktivierung bzw. Anpassung von Sicherheitsmechanismen betreffen, nicht aber die dynamische Verbindungssteuerung selbst. Keine der Anforderungen beschreibt jedoch die eigentliche Kernaussage der GS++-Anforderung, nämlich Verbindungen anhand dynamisch ermittelter Kontextmerkmale oder adaptiver Policy-Engines/SDN-Mechanismen zu steuern.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die dynamische Bewertung von Kontextmerkmalen (z. B. Device Posture, Standort, Auslastung, Risikobewertung), die adaptive Entscheidungslogik bei unveränderten Regeln sowie der explizite Bezug zu software-definierten bzw. kontextabhängigen Verbindungen. Die Kandidaten beschreiben überwiegend statische Allowlist-, Segmentierungs- oder Firewall-Regeln.

### ARCH.5.1.8 — Inspektion verschlüsselter Verbindungen
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A21` [Standard] Temporäre Entschlüsselung des Datenverkehrs — _NET.3.2 Firewall_
  - `NET.1.1.A12` [Basis] Absicherung ausgehender interner Kommunikation zum Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A20` [Standard] Absicherung von grundlegenden Internetprotokollen — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A21=0.47, NET.1.1.A12=0.34, NET.3.2.A20=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9300 gs_ids=NET.3.2.A21
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6855 gs_ids=NET.3.2.A20;NET.1.1.A12
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A21 deckt den Kernaspekt der GS++-Anforderung ab, nämlich die temporäre Entschlüsselung verschlüsselter Verbindungen zur Protokollverifikation und Schadsoftwareprüfung mittels TLS-Proxy. Die GS++-Anforderung geht jedoch weiter und fordert allgemein die Inspektion verschlüsselter Verbindungen basierend auf der Art des Inhalts sowie mögliche Inspektion auf Endstellen; diese allgemeine Inhalts- und Endstellenperspektive wird durch NET.3.2.A21 nicht vollständig abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die allgemein formulierte Inhaltssteuerung für verschlüsselte Verbindungen unabhängig von einem konkreten TLS-Proxy-Einsatz sowie die explizite Inspektion auf den Endstellen der Verbindungen. Ebenfalls fehlt die breitere Architekturvorgabe für externe Netzanschlüsse.

### ASST.2.1.1 — Informationsverantwortung
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `ORP.1.A2` [Basis] Zuweisung der Zuständigkeiten — _ORP.1 Organisation_
- **Begründung:** Gemittelte Kandidatenscores: ORP.1.A2=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9300 gs_ids=ORP.1.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.1.A2 deckt die wesentlichen Inhalte der GS++-Anforderung ASST.2.1.1 ab: Es fordert, dass für Geschäftsprozesse, Anwendungen und IT-Systeme festgelegt wird, wer zuständig ist, und dass alle Mitarbeitenden darüber informiert sind. Damit ist die Zuweisung einer internen Zuständigkeit bzw. Asset Ownership für Informationen und die damit verbundene Verantwortung für deren Schutz inhaltlich getroffen. Die von ASST.2.1.1 beschriebene Zuordnung der Verarbeitung und des Schutzes von Informationen ist durch diese allgemeine Zuständigkeitsfestlegung abgedeckt.
- **Lücken:** [gpt-5.4-mini] Die Konkretisierung auf 'Informationen und Assets für Daten' sowie die alternative Umsetzung über dezentrales Nachhalten oder Gruppierung nach Assets wird in ORP.1.A2 nicht ausdrücklich beschrieben, ist aber für die wesentliche Zielsetzung nicht erforderlich.

### ASST.2.2.1 — Aufdecken unautorisierter IT-Systeme
- **Confidence:** 0.39
- **Gemappte GS-Anforderungen:**
  - `NET.2.1.A14` [Standard] Regelmäßige Audits der WLAN-Komponenten — _NET.2.1 WLAN-Betrieb_
  - `NET.2.2.A1` [Basis] Erstellung einer Nutzungsrichtlinie für WLAN — _NET.2.2 WLAN-Nutzung_
  - `OPS.1.1.1.A6` [Standard] Durchführung des IT-Asset-Managements — _OPS.1.1.1 Allgemeiner IT-Betrieb_
- **Begründung:** Gemittelte Kandidatenscores: NET.2.1.A14=0.39, NET.2.2.A1=0.39, OPS.1.1.1.A6=0.39
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7800 gs_ids=NET.2.2.A1;NET.2.1.A14;OPS.1.1.1.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.2.2.A1 passt inhaltlich am ehesten, weil die WLAN-Nutzungsrichtlinie explizit das Verbot ungenehmigter Access Points enthält und damit organisatorisch auf das Verhindern unautorisierter Netzkomponenten abzielt. NET.2.1.A14 ergänzt dies durch regelmäßige Audits der WLAN-Komponenten und die Überprüfung auf Abweichungen, was eine Erkennung unbekannter oder unerlaubter WLAN-Infrastruktur unterstützt. OPS.1.1.1.A6 beschreibt das Erstellen und Pflegen einer vollständigen IT-Asset-Übersicht und kann unautorisierte Systeme nur indirekt über Inventarisierung sichtbar machen. Zusammen decken die Kandidaten Teile des Ziels ab, unautorisierte IT-Systeme zu erkennen und zu dokumentieren, aber nicht vollständig die geforderte aktive Aufdeckung mittels z. B. Netzscans, passiver Analysen oder spezieller Erkennungswerkzeuge sowie die Behandlung gefundener Systeme.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkreten technischen Erkennungsverfahren (aktive Netzscans, passive Traffic-Analysen, Erkennung unbekannter WLAN-APs mit Spezialwerkzeugen) sowie die vorgeschlagene Reaktion auf gefundene Systeme (Entfernung aus dem Netz, Quarantäne oder nachträgliche Autorisierung). OPS.1.1.1.A6 adressiert primär Inventarisierung, nicht das aktive Aufdecken.

### ASST.4.4 — Nachweis des Zugangs
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `DER.3.1.A27` [Standard] Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen — _DER.3.1 Audits und Revisionen_
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.3.2.A6` [Basis] Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: DER.3.1.A27=0.42, OPS.2.3.A7=0.42, OPS.3.2.A6=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=DER.3.1.A27;OPS.3.2.A6;OPS.2.3.A7
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.3.1.A27 passt inhaltlich am ehesten, weil es die nachvollziehbare, revisionssichere Ablage und Aufbewahrung von Unterlagen zu Audits und Revisionen verlangt und damit den Aspekt der manipulationssicheren Archivierung eines Zugangsnachweises adressiert. OPS.3.2.A6 und OPS.2.3.A7 regeln bei der Beendigung von Outsourcing-Verhältnissen die dokumentierte Rückgabe von Informationen/Daten sowie die Prüfung der Aufhebung von Zugangsrechten; damit enthalten sie einen Dokumentationsbezug rund um Zugriff/Zugang, aber keinen eigentlichen Nachweis des Zugangs einer Nachricht. Insgesamt wird der Kernaspekt 'Nachweis des Zugangs' nur teilweise abgedeckt, da die Kandidaten keine konkrete Anforderung an Empfangsbestätigung, Zugangsprotokollierung zu einer konkreten Nachricht oder die Dokumentation von Ziel-/Versanddaten als Zugangsnachweis enthalten.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind insbesondere die konkrete Protokollierung des Zugangs einer bestimmten Nachricht an den Empfänger, Empfangsbestätigungen bzw. systematische Zugangsprotokolle für Nachrichten, die Zuordnung zu Titel sowie Versand- und Zieladressen und die explizite Beweisfunktion im Streitfall für rechtlich relevante Kommunikation.

### ASST.6.1 — Abhandenkommen
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `DER.2.1.A7` [Standard] Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `SYS.3.1.A12` [Standard] Verlustmeldung für Laptops — _SYS.3.1 Laptops_
  - `SYS.3.3.A2` [Basis] Sperrmaßnahmen bei Verlust eines Mobiltelefons — _SYS.3.3 Mobiltelefon_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.1.A7=0.46, SYS.3.1.A12=0.46, SYS.3.3.A2=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9100 gs_ids=DER.2.1.A7;SYS.3.3.A2;SYS.3.1.A12
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.2.1.A7 deckt den organisatorischen Kern ab, da dort eine definierte, dokumentierte Vorgehensweise zur Behandlung von Sicherheitsvorfällen gefordert wird. Das passt inhaltlich zu einer Vorgehensweise beim Abhandenkommen von Assets, ist aber allgemein auf Sicherheitsvorfälle bezogen. SYS.3.3.A2 deckt den konkreten Umgang beim Verlust eines Mobiltelefons ab, insbesondere SIM-Kartensperre sowie ggf. Fernlöschung/-sperrung und damit einen wichtigen Teilaspekt der geforderten Maßnahmen beim Abhandenkommen eines Assets. SYS.3.1.A12 deckt die Verlustmeldung für Laptops, klare Meldewege und die Prüfung wieder aufgetauchter Geräte auf Manipulation ab und trifft damit ebenfalls einen konkreten Teilaspekt der Asset-Verlustbehandlung. Zusammen adressieren die drei Anforderungen zentrale Reaktionsaspekte nach Verlust, aber nicht allgemein alle Asset-Arten und nicht die vollständige, institutionelle Verlustbehandlungsprozedur für sämtliche Informationswerte und Assets.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind eine asset-übergreifende, einheitliche Vorgehensweise für alle Informationswerte und Assets, die Verantwortlichkeiten und Eskalationsschritte für alle Verlustszenarien sowie explizite Maßnahmen wie Meldung an Fundbüros/Ermittlungsbehörden, systematische Änderung betroffener Zugangsdaten und Sperrung weiterer Authentisierungsmittel außerhalb von Mobiltelefonen. Zudem sind die Kandidaten teils auf einzelne Asset-Typen (Mobiltelefon, Laptop) beschränkt.

### ASST.7.1 — Nicht mehr benötigte Anwendungen
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `APP.6.A13` [Standard] Deinstallation von Software — _APP.6 Allgemeine Software_
  - `SYS.1.9.A15` [Standard] Härtung des Terminalservers — _SYS.1.9 Terminalserver_
  - `SYS.2.1.A16` [Standard] Deaktivierung und Deinstallation nicht benötigter Komponenten und Kennungen — _SYS.2.1 Allgemeiner Client_
  - `SYS.3.2.2.A7` [Standard] Installation von Apps — _SYS.3.2.2 Mobile Device Management (MDM)_
  - `SYS.4.4.A13` [Standard] Deaktivierung und Deinstallation nicht benötigter Komponenten — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.6.A13=0.45, SYS.1.9.A15=0.45, SYS.2.1.A16=0.45, SYS.3.2.2.A7=0.45, SYS.4.4.A13=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9000 gs_ids=APP.6.A13;SYS.2.1.A16;SYS.1.9.A15;SYS.3.2.2.A7;SYS.4.4.A13
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] APP.6.A13 deckt die Deinstallation von Software einschließlich der Entfernung nicht mehr benötigter Dateien und Systemeinträge ab und passt damit direkt zum Kernaspekt der nicht mehr benötigten Anwendungsinstanz. SYS.2.1.A16 erweitert dies auf Clients und nennt ausdrücklich die Deinstallation nicht benötigter Anwendungen, Programme und Dienste sowie nicht benötigter Kennungen. SYS.1.9.A15 ist inhaltlich sehr nah für Terminalserver, da dort nicht benötigte Anwendungen entfernt oder ihre Ausführung unterbunden werden soll. SYS.3.2.2.A7 adressiert die Installation, Deinstallation und Aktualisierung von Apps über MDM auf mobilen Endgeräten und trifft damit den mobilen Teilaspekt. SYS.4.4.A13 fordert für IoT-Geräte die Deaktivierung oder Deinstallation nicht benötigter Protokolle, Dienste und Anwendungen und ist damit ebenfalls ein enger Teiltreffer. Insgesamt wird der Deinstallationsaspekt technisch abgedeckt, aber nicht vollständig die in der GS++-Anforderung enthaltenen organisatorischen und weitergehenden Punkte wie geregelter Gesamtprozess, zugehörige Berechtigungen/Zugriffsrechte, Cloud-Datenlöschung bei nicht kontrollierten Instanzen und die breite Asset-/Anwendungsperspektive über alle Umgebungen hinweg.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind: geregelter End-to-End-Prozess zur vollständigen und nachvollziehbaren Entfernung inklusive Konfigurationsbereinigung als explizite Prozessvorgabe, die Löschung zugehöriger lokaler und Cloud-Daten, der Entzug nicht mehr benötigter Berechtigungen/Zugriffsrechte sowie der allgemeine, bausteinübergreifende Anwendungsbezug für alle Plattformen und Betriebsformen.

### ASST.7.6 — Autorisierung von Veräußerungen
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `CON.6.A11` [Basis] Löschung und Vernichtung von Datenträgern durch externe Dienstleistende — _CON.6 Löschen und Vernichten_
  - `CON.6.A2` [Basis] Ordnungsgemäßes Löschen und Vernichten von schützenswerten Betriebsmitteln und Informationen — _CON.6 Löschen und Vernichten_
  - `SYS.3.1.A7` [Standard] Geregelte Übergabe und Rücknahme eines Laptops — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: CON.6.A11=0.43, CON.6.A2=0.43, SYS.3.1.A7=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=SYS.3.1.A7;CON.6.A2;CON.6.A11
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] SYS.3.1.A7 deckt die geregelte Übergabe eines Laptops vor Weitergabe ab und nennt explizit die sichere Löschung schutzwürdiger Daten vor der Weitergabe. CON.6.A2 deckt den Prozessaspekt des sicheren Löschens und Vernichtens von schutzbedürftigen Informationen und Datenträgern ab, einschließlich einer klar geregelten Vorgehensweise. CON.6.A11 deckt die sichere und nachvollziehbare Durchführung der Löschung/Vernichtung durch externe Dienstleistende ab. Zusammen wird damit ein Teil der Veräußerungsvorbereitung und der sicheren Behandlung von Daten/Datenträgern adressiert. Die eigentliche GS++-Kernforderung der Autorisierung jeder Veräußerung von Assets durch eine zuständige Stelle bzw. Rolle vor der endgültigen Abgabe wird jedoch in keiner Kandidatenanforderung ausdrücklich geregelt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die eigentliche Freigabe/Autorisierung von Veräußerungen als organisatorischer Entscheidungsschritt, die Festlegung von Rollen und Genehmigungstiefen (z. B. Asset-Owner, ISB, Vier-Augen-Prinzip je Schutzbedarf) sowie die Kontrolle von Veräußerungen aller Asset-Typen über Datenträger hinaus (z. B. Rückgabe an Leasing, Recycling, Lizenzübertragung).

### BER.1.1.3 — Bekanntgabe
- **Confidence:** 0.41
- **Gemappte GS-Anforderungen:**
  - `DER.1.A7` [Standard] Schulung von Zuständigen — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `NET.3.2.A1` [Basis] Erstellung einer Sicherheitsrichtlinie — _NET.3.2 Firewall_
  - `OPS.1.2.5.A6` [Standard] Erstellung einer Richtlinie für die Fernwartung — _OPS.1.2.5 Fernwartung_
- **Begründung:** Gemittelte Kandidatenscores: DER.1.A7=0.41, NET.3.2.A1=0.41, OPS.1.2.5.A6=0.41
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8300 gs_ids=NET.3.2.A1;OPS.1.2.5.A6;DER.1.A7
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A1 passt inhaltlich, weil dort ausdrücklich gefordert wird, dass die spezifische Richtlinie allen zuständigen Mitarbeitenden bekannt sein muss. OPS.1.2.5.A6 passt ebenfalls, da die Richtlinie zur Fernwartung allen Zuständigen bekannt sein SOLL, die an Konzeption, Aufbau und Betrieb beteiligt sind. DER.1.A7 passt nur eingeschränkt, weil Schulungen für Zuständige zu Ereignismeldungen gefordert werden; das adressiert zwar die Bekanntgabe von Verfahren indirekt über Qualifizierung, aber nicht die explizite Information über Regeln und Verfahren. Gemeinsam decken die Kandidaten den Aspekt ab, dass zuständige Personen über Verfahren/Regelungen informiert und diese bekannt gemacht werden, jedoch nicht allgemeingültig für alle Berechtigungs-Prozesse und nicht mit dem expliziten Fokus auf Onboarding und automatische Benachrichtigung bei Änderungen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine, domänenübergreifende Bekanntgabe von Berechtigungsverfahren und -regelungen an alle zuständigen Rollen sowie die explizite Anforderung, Änderungen systematisch per Benachrichtigung bekanntzugeben. Die Kandidaten sind zudem auf konkrete Fachdomänen (Firewall, Fernwartung, Ereignismeldungen) begrenzt und ersetzen keine allgemeine Regel zur Informationspflicht im Berechtigungsmanagement.

### BER.1.2 — Regelmäßige Überprüfung
- **Confidence:** 0.41
- **Gemappte GS-Anforderungen:**
  - `DER.1.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `DER.1.A13` [Standard] Regelmäßige Audits der Detektionssysteme — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `OPS.1.1.1.A2` [Basis] Festlegung von Rollen und Berechtigungen für den IT-Betrieb — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `OPS.1.1.5.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für die Protokollierung — _OPS.1.1.5 Protokollierung_
  - `ORP.5.A8` [Standard] Regelmäßige Überprüfungen des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `APP.4.3.A20` [Standard] Regelmäßige Audits — _APP.4.3 Relationale Datenbanken_
  - `OPS.1.2.2.A13` [Standard] Regelmäßige Revision der Archivierungsprozesse — _OPS.1.2.2 Archivierung_
- **Begründung:** Gemittelte Kandidatenscores: DER.1.A1=0.41, DER.1.A13=0.41, OPS.1.1.1.A2=0.41, OPS.1.1.5.A1=0.41, ORP.5.A8=0.41, APP.4.3.A20=0.33, OPS.1.2.2.A13=0.33
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8200 gs_ids=OPS.1.1.1.A2;ORP.5.A8;DER.1.A1;DER.1.A13;OPS.1.1.5.A1
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6600 gs_ids=APP.4.3.A20;OPS.1.2.2.A13
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung BER.1.2 verlangt eine regelmäßige und anlassbezogene Überprüfung von Berechtigungsverfahren und Regelungen auf Aktualität. Inhaltlich am nächsten kommen dafür OPS.1.1.1.A2, da dort Rollen- und Berechtigungskonzepte für den IT-Betrieb regelmäßig geprüft und an aktuelle Gegebenheiten angepasst werden müssen, sowie ORP.5.A8, weil dort Verfahren zur regelmäßigen Überprüfung des Compliance-Managements und der zugehörigen Anforderungen/Maßnahmen auf Effizienz und Effektivität gefordert werden. Ebenfalls passend sind DER.1.A1 und DER.1.A13, da sie für die Detektion eine spezifische Sicherheitsrichtlinie bzw. Detektionssysteme regelmäßig auf korrekte Umsetzung, Aktualität und Wirksamkeit überprüfen. OPS.1.1.5.A1 passt ebenfalls, weil die Protokollierungsrichtlinie regelmäßig überprüft werden muss. Gemeinsam decken diese Anforderungen den Aspekt der regelmäßigen Überprüfung von Regeln/Verfahren gut ab.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die anlassbezogene Überprüfung ausdrücklich als Reaktion auf konkrete Ereignisse sowie der spezielle Fokus auf Berechtigung im Sinne des übergreifenden Berechtigungsprozesses der Institution; außerdem ist die GS++-Anforderung allgemeiner formuliert und nicht auf IT-Betrieb, Compliance, Detektion oder Protokollierung beschränkt. Die Kandidaten liefern überwiegend bereichsspezifische Überprüfungsanforderungen, aber keine vollumfängliche, allgemeine Regelung zur regelmäßigen und ereignisgetriebenen Überprüfung aller Berechtigungsverfahren und -regelungen.

### BER.2.5 — Deaktivierung bei Weggang
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `DER.3.1.A24` [Standard] Abschluss des Audits oder der Revision — _DER.3.1 Audits und Revisionen_
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.3.2.A6` [Basis] Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: DER.3.1.A24=0.47, OPS.2.3.A7=0.47, OPS.3.2.A6=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9300 gs_ids=OPS.2.3.A7;OPS.3.2.A6;DER.3.1.A24
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.2.3.A7 und OPS.3.2.A6 passen inhaltlich nur in Teilen, weil sie das Aufheben von Zugangs-/Zugriffsrechten bei Beendigung eines Outsourcing-Verhältnisses bzw. die Rückgabe/Löschung von Informationen und Daten nach Vertragsende behandeln. DER.3.1.A24 ist ebenfalls nur teilweise passend, weil dort genehmigte Zugriffe eines Auditteams nach Abschluss wieder deaktiviert oder gelöscht werden müssen. Alle drei Anforderungen treffen den Aspekt der Deaktivierung bzw. Beendigung von Berechtigungen nach einem Ereignis, aber nicht spezifisch den Weggang von Nutzenden bzw. die zugeordnete Identität im Personal-/Berechtigungskontext. Die GS++-Anforderung verlangt explizit, dass die Berechtigung die Identität bei Weggang deaktiviert oder löscht; das ist in den Kandidaten nur indirekt und kontextfremd abgebildet.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die spezifische Zuordnung von Berechtigung zu Identität, der personelle Weggang (z. B. Kündigung, Elternzeit, Sabbatical) sowie die explizite Pflicht zur Deaktivierung/Löschung der Identität selbst. Die Kandidaten regeln überwiegend Rechteentzug in Outsourcing- oder Audit-Kontexten, nicht das allgemeine Identitätsmanagement für ausscheidende Nutzende.

### BER.3.15 — Keine Gruppenkonten
- **Confidence:** 0.39
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.2.A22` [Basis] Trennung von administrativen und anderen Tätigkeiten — _OPS.1.1.2 Ordnungsgemäße IT-Administration_
  - `SYS.2.4.A3` [Basis] Verwendung geeigneter Konten — _SYS.2.4 Clients unter macOS_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.2.A22=0.39, SYS.2.4.A3=0.39
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7800 gs_ids=SYS.2.4.A3;OPS.1.1.2.A22
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] SYS.2.4.A3 trifft den Kernaspekt der Anforderung insofern, als für die normale Nutzung getrennte Benutzerkonten statt eines gemeinsam genutzten Kontos vorgesehen sind; das reduziert faktisch die Nutzung von Gruppenkonten. OPS.1.1.2.A22 ergänzt dies, indem die Zugangskennungen für administrative Tätigkeiten von anderen Nutzungskontexten getrennt werden sollen, was ebenfalls gegen die Verwendung eines einzigen Kontos durch mehrere Zwecke spricht. Beide Anforderungen untersagen jedoch nicht explizit Gruppenkonten und decken nicht den allgemeinen Grundsatz ab, dass Berechtigung Gruppenkonten generell untersagen soll.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist das explizite Verbot bzw. die generelle Untersagung von Gruppenkonten für alle Kontotypen und Kontexte. Die Kandidaten verlangen lediglich getrennte Konten bzw. einen getrennten Administrationskontext, aber kein ausdrückliches Verbot gemeinsam genutzter Zugangskonten.

### BER.6.8 — Kriterien für die Qualität von Passwörtern
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `ORP.4.A23` [Basis] Regelung für passwortverarbeitende Anwendungen und IT-Systeme — _ORP.4 Identitäts- und Berechtigungsmanagement_
- **Begründung:** Gemittelte Kandidatenscores: ORP.4.A23=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=ORP.4.A23
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.4.A23 deckt den Passwort-Lebenszyklus und zentrale Qualitätsaspekte von Passwörtern in passwortverarbeitenden Anwendungen ab: Es fordert u. a. den Einsatz ausreichend starker Passwörter, die Berücksichtigung der maximal möglichen Passwortlänge sowie sichere Speicherung und den Umgang mit Passwortwechseln. Damit gibt es eine inhaltliche Überschneidung zur Grundschutz++-Anforderung BER.6.8, die Kriterien für die Passwortqualität anhand von Lebensdauer und Angriffsmöglichkeiten festlegen soll. Die wesentliche, explizite Systematik der Grundschutz++-Anforderung – Kriterien zur Qualität von Passwörtern abhängig von Lebensdauer, Angriffslage und begleitenden Sicherheitsmaßnahmen (z. B. Entropie, Länge, Symbole, MFA, maximale Versuche) – wird durch ORP.4.A23 jedoch nicht vollständig vorgegeben. Die übrigen Kandidaten behandeln andere Themen wie MFA allgemein (CON.10.A16, ORP.4.A10, OPS.1.2.5.A17) oder Passwortzurücksetzen (ORP.4.A11) und bilden die geforderte Festlegung von Qualitätskriterien nicht direkt ab.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die explizite Festlegung von Qualitätskriterien nach Lebensdauer und Angriffsmöglichkeiten, konkrete Parameter wie Entropie, Symbolvielfalt oder differenzierte Regeln je Anwendung/Zugang sowie die Einbettung der Kriterien in ein allgemeines Berechtigungs-/Passwortkonzept. MFA wird nur als begleitender Faktor erwähnt, nicht als Teil der Passwortqualitätskriterien selbst.

### BER.7.16.3 — Erneuerung
- **Confidence:** 0.39
- **Gemappte GS-Anforderungen:**
  - `APP.3.6.A17` [Standard] Einsatz von DNSSEC — _APP.3.6 DNS-Server_
  - `CON.1.A4` [Basis] Geeignetes Schlüsselmanagement — _CON.1 Kryptokonzept_
  - `DER.2.3.A4` [Basis] Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln — _DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle_
- **Begründung:** Gemittelte Kandidatenscores: APP.3.6.A17=0.39, CON.1.A4=0.39, DER.2.3.A4=0.39
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7800 gs_ids=CON.1.A4;DER.2.3.A4;APP.3.6.A17
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.1.A4 deckt den allgemeinen Rahmen des Schlüsselmanagements ab, insbesondere die Sicherstellung von Integrität und Authentizität öffentlicher Schlüssel sowie die rechtzeitige Erneuerung zeitlich begrenzter Schlüssel/Zertifikate. DER.2.3.A4 passt für den Fall kompromittierter TLS-Schlüssel oder CA-Strukturen und fordert die Neuerzeugung sowie das Sperren/Rückrufen betroffener Schlüssel und Zertifikate. APP.3.6.A17 ist inhaltlich verwandt, weil dort die regelmäßige Erneuerung der für DNSSEC verwendeten Schlüssel vorgesehen ist. Keine der Anforderungen beschreibt jedoch den spezifischen Prüfschritt bei der Erneuerung einer Beglaubigung, also die explizite Validierung des Schlüssels anhand von Beglaubigungsvorgaben (z. B. Fingerprint-, Signatur- oder Sperrlistenprüfung).
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkrete Prüfhandlung bei der Erneuerung der Beglaubigung und die spezifische Vertrauensketten-/Zertifikatsvalidierung im Sinne eines Tests des Schlüssels vor erneuter Beglaubigung. Die Kandidaten behandeln eher allgemeines Schlüsselmanagement, Erneuerung, Wechsel oder Reaktion auf Kompromittierung.

### BER.7.16.6 — Revocationstatus
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `DER.2.3.A4` [Basis] Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln — _DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.3.A4=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9700 gs_ids=DER.2.3.A4
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.2.3.A4 deckt den Kern der GS++-Anforderung ab: Dort wird gefordert, kompromittierte kryptografische Schlüssel und Zertifikate zuverlässig zu sperren und zurückzurufen. Das entspricht inhaltlich dem geforderten Dokumentieren des Revocationstatus, also der Information, ob ein Schlüssel zurückgezogen wurde. Die GS++-Anforderung ist dabei eine engere, statusbezogene Ausprägung innerhalb derselben Domäne des Schlüssel-/Zertifikats-Revocationsmanagements.
