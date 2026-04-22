# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:46:35

**Gesamt:** 20 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 18 |
| Keine Abdeckung | 2 |

## Teilweise abgedeckt (18)

### ARCH.1.1.1 — Dokumentation
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `APP.6.A10` [Standard] Erstellung einer Sicherheitsrichtlinie für den Einsatz der Software — _APP.6 Allgemeine Software_
  - `APP.7.A6` [Standard] Dokumentation der Anforderungen an die Individualsoftware — _APP.7 Entwicklung von Individualsoftware_
  - `CON.8.A12` [Standard] Ausführliche Dokumentation — _CON.8 Software-Entwicklung_
  - `IND.1.A11` [Standard] Sichere Beschaffung und Systementwicklung — _IND.1 Prozessleit- und Automatisierungstechnik_
  - `IND.2.7.A1` [Basis] Erfassung und Dokumentation — _IND.2.7 Safety Instrumented Systems_
  - `NET.1.2.A12` [Standard] Ist-Aufnahme und Dokumentation des Netzmanagements — _NET.1.2 Netzmanagement_
  - `SYS.1.1.A11` [Standard] Festlegung einer Sicherheitsrichtlinie für Server — _SYS.1.1 Allgemeiner Server_
  - `SYS.4.4.A6` [Standard] Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.6.A10=0.44, APP.7.A6=0.44, CON.8.A12=0.44, IND.1.A11=0.44, IND.2.7.A1=0.44, NET.1.2.A12=0.44, SYS.1.1.A11=0.44, SYS.4.4.A6=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=APP.6.A10;CON.8.A12;APP.7.A6;NET.1.2.A12;IND.2.7.A1;SYS.1.1.A11;SYS.4.4.A6;IND.1.A11
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.1.1.1 verlangt, Verfahren und Regelungen zu dokumentieren. Das wird inhaltlich von APP.6.A10 abgedeckt, da dort die Regelungen zum Einsatz und Betrieb der Software in einer Sicherheitsrichtlinie zusammengefasst werden sollen, und von CON.8.A12, weil dort Projekt-, Funktions- und Schnittstellendokumentationen sowie die aktuelle Dokumentation gefordert werden. Auch APP.7.A6, NET.1.2.A12, IND.2.7.A1, SYS.1.1.A11, SYS.4.4.A6 und IND.1.A11 enthalten jeweils Anforderungen, bestimmte Regelungen, Richtlinien oder Umsetzungsstände zu dokumentieren. Diese Kandidaten treffen jedoch nur den generellen Dokumentationsaspekt bzw. dokumentieren jeweils spezifische fachliche Inhalte in einzelnen Domänen. Sie decken nicht die allgemeine, domänenübergreifende Pflicht ab, die Verfahren und Regelungen der Architektur als solche zu dokumentieren.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der übergreifende Architekturbezug: gefordert ist die Dokumentation der Architektur-Verfahren und -Regelungen als allgemeine, rollen- und zielgruppenorientierte verbindliche Referenz. Die Kandidaten beschreiben überwiegend domänenspezifische Dokumentationen (Software, Netzwerk, Server, IoT, OT, Audits) oder die Dokumentation von Ergebnissen/Anforderungen, aber nicht die allgemeine Dokumentation aller Architektur-Verfahren und -Regelungen in der geforderten Breite und Zielgruppenorientierung.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.81
- **Gemappte GS-Anforderungen:**
  - `NET.3.3.A11` [Standard] Sichere Anbindung eines externen Netzes — _NET.3.3 VPN_
  - `CON.7.A7` [Basis] Sicherer Remote-Zugriff auf das Netz der Institution — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `CON.7.A8` [Basis] Sichere Nutzung von öffentlichen WLANs — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `INF.10.A6` [Standard] Einrichtung sicherer Netzzugänge — _INF.10 Besprechungs-, Veranstaltungs- und Schulungsräume_
  - `NET.1.1.A10` [Basis] DMZ-Segmentierung für Zugriffe aus dem Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A18` [Standard] P-A-P-Struktur für die Internet-Anbindung — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A9` [Basis] Grundlegende Absicherung der Kommunikation mit nicht vertrauenswürdigen Netzen — _NET.1.1 Netzarchitektur und -design_
  - `SYS.3.1.A8` [Standard] Sicherer Anschluss von Laptops an Datennetze — _SYS.3.1 Laptops_
  - `SYS.3.1.A9` [Basis] Sicherer Fernzugriff mit Laptops — _SYS.3.1 Laptops_
  - `SYS.3.2.1.A28` [Standard] Verwendung der Filteroption für Webseiten — _SYS.3.2.1 Allgemeine Smartphones und Tablets_
  - `NET.1.1.A11` [Basis] Absicherung eingehender Kommunikation vom Internet in das interne Netz — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.3.A11=0.81, CON.7.A7=0.45, CON.7.A8=0.45, INF.10.A6=0.45, NET.1.1.A10=0.45, NET.1.1.A18=0.45, NET.1.1.A4=0.45, NET.1.1.A9=0.45, SYS.3.1.A8=0.45, SYS.3.1.A9=0.45, SYS.3.2.1.A28=0.45, NET.1.1.A11=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9000 gs_ids=NET.1.1.A4;NET.1.1.A10;NET.1.1.A18;NET.1.1.A9;SYS.3.1.A9;CON.7.A7;CON.7.A8;SYS.3.1.A8;NET.3.3.A11;INF.10.A6;SYS.3.2.1.A28
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.1 verlangt, externe Netzanschlüsse in der Architektur zu begrenzen, um unerwünschte Ein-/Ausleitungen und die Angriffsfläche zu reduzieren. Dies wird inhaltlich am ehesten durch NET.1.1.A4 (Netztrennung in Zonen), NET.1.1.A10 (DMZ-Segmentierung für Zugriffe aus dem Internet), NET.1.1.A18 (P-A-P-Struktur für die Internet-Anbindung) und NET.1.1.A9 (Absicherung nicht vertrauenswürdiger Netze) abgedeckt, da diese Anforderungen die strukturelle Absicherung und Segmentierung von Außenanbindungen und Internetzugängen behandeln. Ergänzend passen CON.7.A7, CON.7.A8, SYS.3.1.A9 und NET.3.3.A11, weil sie für mobile bzw. externe Zugriffe sichere VPN-/Kommunikationskanäle statt direkter Internetnutzung vorsehen. INF.10.A6 und SYS.3.1.A8 adressieren außerdem das Verhindern paralleler oder unkontrollierter Verbindungen zwischen internem Netz und Internet in bestimmten Einsatzkontexten. SYS.3.2.1.A28 ergänzt den Aspekt, mobile Endgeräte über VPN in die institutionelle Proxy-/Filter-Infrastruktur einzubinden. Dennoch decken die Kandidaten nicht vollständig den architektonischen Soll-Aspekt "Verbindungen über externe Netzanschlüsse einschränken" in generischer Form ab, insbesondere nicht als allgemeine Vorgabe für alle Netzsegmente und alle Arten externer Anschlüsse, sondern überwiegend für Internet-/VPN-/WLAN- und einzelne Szenarien.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind allgemeine, domänenübergreifende Architekturregeln zur Einschränkung aller externen Netzanschlüsse unabhängig vom Nutzungsszenario. Die Kandidaten fokussieren vor allem Internet-, VPN-, DMZ- und mobile Zugriffe sowie einzelne Raum-/Laptopszenarien. Eine explizite generische Regel, externe Netzanschlüsse insgesamt zu minimieren bzw. konsequent zu kontrollieren, fehlt.

### ARCH.2.2.11 — Physische Segmentierung
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.4.2.A4` [Basis] Einschränkung der Erreichbarkeit über VoIP — _NET.4.2 VoIP_
  - `OPS.1.1.2.A16` [Standard] Erweiterte Sicherheitsmaßnahmen für Administrationszugänge — _OPS.1.1.2 Ordnungsgemäße IT-Administration_
  - `SYS.1.5.A15` [Standard] Betrieb von Gast-Betriebssystemen mit unterschiedlichem Schutzbedarf — _SYS.1.5 Virtualisierung_
  - `SYS.1.5.A4` [Basis] Sichere Konfiguration eines Netzes für virtuelle Infrastrukturen — _SYS.1.5 Virtualisierung_
  - `SYS.1.5.A9` [Standard] Netzplanung für virtuelle Infrastrukturen — _SYS.1.5 Virtualisierung_
  - `SYS.1.8.A15` [Standard] Sichere Trennung von Mandanten in Speicherlösungen — _SYS.1.8 Speicherlösungen_
  - `SYS.2.5.A2` [Basis] Planung der verwendeten Netze für virtuelle Clients — _SYS.2.5 Client-Virtualisierung_
  - `SYS.2.6.A4` [Standard] Netzsegmentierung der VDI-Komponenten — _SYS.2.6 Virtual Desktop Infrastructure_
  - `NET.1.1.A22` [Standard] Spezifikation des Segmentierungskonzepts — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A23` [Standard] Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A31` _(nicht im Korpus gefunden)_
  - `NET.1.1.A33` _(nicht im Korpus gefunden)_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.43, NET.1.1.A4=0.43, NET.4.2.A4=0.43, OPS.1.1.2.A16=0.43, SYS.1.5.A15=0.43, SYS.1.5.A4=0.43, SYS.1.5.A9=0.43, SYS.1.8.A15=0.43, SYS.2.5.A2=0.43, SYS.2.6.A4=0.43, NET.1.1.A22=0.34, NET.1.1.A23=0.34, NET.1.1.A31=0.34, NET.1.1.A33=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8700 gs_ids=SYS.1.5.A4;NET.1.1.A4;INF.14.A6;SYS.1.5.A9;SYS.1.5.A15;SYS.1.8.A15;OPS.1.1.2.A16;NET.4.2.A4;SYS.2.5.A2;SYS.2.6.A4
[manual:gspp_compliance_v3approach] coverage=teilweise confidence=0.6711 gs_ids=NET.1.1.A31;NET.1.1.A23;NET.1.1.A33;NET.1.1.A22
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.11 fordert physische Segmentierung bzw. physische Einschränkung von Verbindungen zwischen Netzen. Dies wird inhaltlich von mehreren klassischen Anforderungen nur teilweise abgedeckt: SYS.1.5.A4 und NET.1.1.A4 adressieren explizit, dass bestehende Sicherheitsmechanismen bzw. Zonen nicht über virtuelle Netze umgangen werden dürfen und Netze/Zonen getrennt werden müssen; INF.14.A6 verlangt die Trennung und kontrollierte Kommunikation zwischen GA- und übrigen Netzen, teils sogar auf Netzebene; SYS.1.5.A9 fordert Planung und sichere Trennung von Netzsegmenten in virtuellen Infrastrukturen; SYS.1.5.A15 und SYS.1.8.A15 behandeln die sichere Kapselung/Trennung bei gemeinsam genutzten Virtualisierungs- bzw. Speicherumgebungen; OPS.1.1.2.A16 verlangt die Trennung von Admin-Netzen und produktiven Netzen; NET.4.2.A4 verhindert direkte Verbindungen aus unsicheren Netzen auf VoIP-Komponenten; SYS.2.5.A2 und SYS.2.6.A4 verlangen Netztrennung für virtuelle Clients bzw. VDI-Komponenten. Diese Anforderungen stützen das Ziel, Segmente wirksam voneinander zu trennen, ersetzen aber die GS++-Forderung nach physischer Segmentierung nicht vollständig.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der explizite Fokus auf physische Trennung auf Architektur-Ebene: mehrere Kandidaten setzen nur logische Trennung, Virtualisierungs- oder Firewall-gestützte Segmentierung voraus. Die GS++-Anforderung betont gerade, dass physische Trennung Konfigurationsfehler und Umgehungen reduziert; diese explizite physische Ausprägung wird von den Kandidaten nicht durchgängig gefordert. Außerdem sind einige Kandidaten domänenspezifisch (GA, VDI, VoIP, Administration, Speicher) und daher nicht als allgemeine Abdeckung für alle Netzsegmente ausreichend.

### ARCH.2.2.8 — Segmentierung von Test und Betrieb
- **Confidence:** 0.49
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.6.A13` [Standard] Trennung der Testumgebung von der Produktivumgebung — _OPS.1.1.6 Software-Tests und -Freigaben_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.6.A13=0.49
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9800 gs_ids=OPS.1.1.6.A13
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.6.A13 deckt die GS++-Anforderung inhaltlich direkt ab: Es fordert, dass Software nur in einer vorgesehenen Testumgebung getestet wird und dass diese Testumgebung von der Produktivumgebung getrennt betrieben wird. Damit wird die Segmentierung bzw. Trennung von Test und Betrieb genau adressiert. Die weiteren Kandidaten behandeln andere Themen wie Freigabe von Images, allgemeine Netztrennung oder spezifische System-/Anwendungsarchitekturen und sind für diese Anforderung nicht der passgenaue Primärmacher.

### ARCH.2.2.9 — Segmentierung von IPv4 und IPv6
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A20` [Standard] Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A20=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9200 gs_ids=NET.1.1.A20
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.1.1.A20 passt inhaltlich, weil es die Zuordnung unterschiedlicher IPv4-/IPv6-Endgerätegruppen zu dedizierten Subnetzen verlangt und damit eine Trennung nach Protokollfamilien unterstützt. Die GS++-Anforderung ARCH.2.2.9 fordert jedoch allgemeiner, Verbindungen zwischen IPv4 und IPv6 in der Architektur einzuschränken; das kann auch Maßnahmen auf anderen Ebenen umfassen und ist nicht auf Endgerätegruppen/Subnetze beschränkt. Die übrigen Kandidaten behandeln andere Sachverhalte wie Deaktivierung einzelner Protokolle, Fragmentierungsschutz, Routing-Header, VPN oder allgemeine Segmentierung ohne spezifische IPv4/IPv6-Trennung.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind insbesondere die allgemeine Einschränkung von Verbindungen zwischen IPv4- und IPv6-Segmenten auf Architektur-/Netzebene sowie Maßnahmen jenseits der Subnetzzuordnung von Endgerätegruppen. NET.1.1.A20 adressiert nur die Protokollzuordnung von Endgeräten zu Subnetzen, nicht die umfassende Segmentierung beider Protokollwelten.

### ARCH.5.1.12 — Software-definierte Verbindungen
- **Confidence:** 0.37
- **Gemappte GS-Anforderungen:**
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.3.2.A2` [Basis] Festlegen der Firewall-Regeln — _NET.3.2 Firewall_
  - `NET.3.4.A6` [Standard] Festlegung von Notfallprozessen für NAC — _NET.3.4 Network Access Control_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.37, NET.3.2.A2=0.37, NET.3.4.A6=0.37
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7400 gs_ids=NET.3.2.A2;INF.14.A6;NET.3.4.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A2 passt insofern, als dort verbindliche Filterregeln für Verbindungen zwischen Netzen festgelegt werden und nicht zugelassene Verbindungen unterbunden werden. INF.14.A6 deckt ebenfalls die kontrollierte und reglementierte Kommunikation zwischen getrennten Netzen mit mindestens Firewall-Funktion ab. NET.3.4.A6 ist nur indirekt relevant, weil es um NAC-Mechanismen und deren Notfallverhalten geht; dynamische, kontextabhängige Verbindungsfreigaben werden dadurch jedoch nicht inhaltlich beschrieben. Die GS++-Anforderung ARCH.5.1.12 verlangt jedoch ausdrücklich, dass Verbindungen anhand dynamischer Kriterien bzw. kontextabhängiger, situativ bewerteter Merkmale gesteuert werden. Dieser Kernaspekt wird von den Kandidaten nicht wirklich abgedeckt, da sie überwiegend statische Allowlist-/Firewall- bzw. Segmentierungsregeln beschreiben.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die dynamische, kontextabhängige Bewertung von Verbindungsbedingungen (z. B. Gerätezustand, Standort, Zeit, Risikobewertung), die daraus abgeleitete adaptive Freigabe/Sperrung sowie der explizite Bezug zu software-definierten Verbindungen, SDN oder Policy-Engines. Die genannten Kandidaten regeln primär statische Filterung und Segmentierung.

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
[gpt-5.4-mini] NET.3.2.A21 passt inhaltlich, weil es die temporäre Entschlüsselung verschlüsselter Verbindungen in nicht vertrauenswürdige Netze zum Verifizieren des Protokolls und zur Schadsoftware-Prüfung beschreibt. Das trifft den Kern der Inspektion verschlüsselter Verbindungen mittels TLS-Proxy/Sicherheitsproxy. Die GS++-Anforderung ist jedoch breiter und fordert allgemein die Einschränkung bzw. Inspektion des Inhalts verschlüsselter Verbindungen basierend auf der Art des Inhalts, einschließlich Optionen wie Proxies oder Endstellen-Inspektion; dieser allgemeine Inhalts- und Policy-Aspekt wird durch NET.3.2.A21 nur teilweise abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine Vorgabe zur inhaltsbasierten Einschränkung verschlüsselter Verbindungen unabhängig von konkreter Malware-Prüfung, die explizite Bezugnahme auf die Art des Inhalts sowie die Möglichkeit der Inspektion auf Endstellen. Die Anforderung konzentriert sich auf TLS-Proxy/Entschlüsselung in nicht vertrauenswürdigen Netzen und auf Protokoll-/Malware-Validierung.

### ASST.2.1.1 — Informationsverantwortung
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `ORP.1.A2` [Basis] Zuweisung der Zuständigkeiten — _ORP.1 Organisation_
- **Begründung:** Gemittelte Kandidatenscores: ORP.1.A2=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9700 gs_ids=ORP.1.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.1.A2 passt inhaltlich am besten, weil dort für Geschäftsprozesse, Anwendungen, IT-Systeme usw. verbindlich festgelegt werden muss, wer zuständig ist und die Mitarbeitenden über ihre Zuständigkeiten informiert sein müssen. Das trifft den organisatorischen Kern der Grundschutz++-Anforderung ASST.2.1.1 „Informationsverantwortung“ (Zuweisung von Zuständigkeit/Ownership für Informationen und Assets) sehr direkt. Allerdings adressiert ORP.1.A2 nur die allgemeine Zuweisung von Zuständigkeiten für Objekte und deren Sicherheit, nicht ausdrücklich die spezifische Verantwortlichkeit für die Verarbeitung von Informationen bzw. Asset Ownership im Sinn der Zuordnung der Verantwortung je Information oder Informationsgruppe.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt bzw. nur implizit: explizite Informationsverantwortung für konkrete Informationen/Daten, mögliche dezentrale Nachhaltung der Verantwortung, sowie die alternative Gruppierung von Informationen nach Assets zur Ableitung der Zuständigkeit.

### ASST.2.2.1 — Aufdecken unautorisierter IT-Systeme
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `NET.2.1.A14` [Standard] Regelmäßige Audits der WLAN-Komponenten — _NET.2.1 WLAN-Betrieb_
  - `NET.2.2.A1` [Basis] Erstellung einer Nutzungsrichtlinie für WLAN — _NET.2.2 WLAN-Nutzung_
  - `OPS.3.2.A14` [Standard] Überwachung der Prozesse, Anwendungen und IT-Systeme — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: NET.2.1.A14=0.43, NET.2.2.A1=0.43, OPS.3.2.A14=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=NET.2.2.A1;NET.2.1.A14;OPS.3.2.A14
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.2.2.A1 passt inhaltlich, weil die WLAN-Nutzungsrichtlinie das klare Verbot ungenehmigter Access Points enthält und damit das Ziel unterstützt, unautorisierte IT-Systeme im Netz zu verhindern. NET.2.1.A14 ergänzt dies, da regelmäßige Audits der WLAN-Komponenten ausdrücklich das Prüfen auf korrekt konfigurierte und sicher umgesetzte Maßnahmen vorsehen; Abweichungen sollen untersucht werden. OPS.3.2.A14 passt nur allgemein, weil eine kontinuierliche Überwachung der eingesetzten Prozesse, Anwendungen und IT-Systeme eine Grundlage für das Erkennen unbekannter Systeme sein kann. Die konkrete Forderung der GS++-Anforderung nach Aufdecken unautorisierter IT-Systeme mittels aktiver/passiver Erkennung und anschließender Behandlung (z. B. Quarantäne, Entfernung, Autorisierung) wird durch diese Anforderungen jedoch nicht vollständig abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die explizite technische Detektion unautorisierter IT-Systeme im Netz (z. B. aktive Netzscans, passive Verkehrsanalyse, Erkennung unbekannter WLAN-APs) sowie die konkrete Reaktion auf gefundene Systeme (Entfernen, Quarantäne, nachträgliche Autorisierung).

### ASST.4.4 — Nachweis des Zugangs
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `DER.3.1.A27` [Standard] Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen — _DER.3.1 Audits und Revisionen_
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.3.2.A6` [Basis] Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: DER.3.1.A27=0.45, OPS.2.3.A7=0.45, OPS.3.2.A6=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=OPS.3.2.A6;OPS.2.3.A7;DER.3.1.A27
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.3.2.A6 und OPS.2.3.A7 behandeln Regelungen bei Beendigung eines Outsourcing-Verhältnisses sowie die Rückgabe von Informationen/Daten und die Dokumentation der Löschung. DER.3.1.A27 deckt die nachvollziehbare, revisionssichere Ablage und Aufbewahrung von Unterlagen zu Audits und Revisionen ab. Damit sind die Aspekte Rückverfolgbarkeit, Dokumentation und revisionssichere Aufbewahrung teilweise getroffen, jedoch nicht der eigentliche Kern der GS++-Anforderung ASST.4.4: der Nachweis des Zugangs einer Nachricht an den Empfänger mit protokolliertem Zugang, ggf. inklusive Metadaten/Inhalt, und der Nachweis in rechtlich relevanten Kommunikationskontexten.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind insbesondere: Protokollierung des tatsächlichen Zugangs einer Nachricht beim Empfänger, Empfangs-/Zugangsbestätigung, Nachweis relevanter Kommunikationsmetadaten (z. B. Titel, Versand- und Zieladresse, Zeitpunkt des Zugangs) sowie der konkrete Fokus auf rechtlich relevante Nachrichtenzustellung statt auf Outsourcing-Beendigung oder Archivierung von Auditunterlagen.

### ASST.6.1 — Abhandenkommen
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `DER.2.1.A6` [Basis] Wiederherstellung der Betriebsumgebung nach Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `DER.2.1.A7` [Standard] Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `SYS.3.1.A12` [Standard] Verlustmeldung für Laptops — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.1.A6=0.42, DER.2.1.A7=0.42, SYS.3.1.A12=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=SYS.3.1.A12;DER.2.1.A7;DER.2.1.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] SYS.3.1.A12 deckt den Fall eines verloren gegangenen oder gestohlenen Laptops mit klaren Meldewegen, was direkt zur geforderten Vorgehensweise beim Abhandenkommen von Assets passt. DER.2.1.A7 liefert die generische organisatorische Vorgabe, für Sicherheitsvorfälle eine definierte, dokumentierte Vorgehensweise festzulegen und aktuell zu halten. DER.2.1.A6 ergänzt die unmittelbaren Reaktionsschritte nach einem Sicherheitsvorfall, insbesondere Netztrennung, Sicherung von Spuren und Änderung von Zugangsdaten; diese Maßnahmen sind auch bei abhandengekommenen Assets relevant. Zusammen ergibt sich eine inhaltliche Annäherung an die geforderte Reaktions- und Behandlungsroutine nach Verlustereignissen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die asset-spezifischen Maßnahmen über Laptops/Mobiltelefone hinaus, z. B. Ortung, Fernlöschung/-sperrung für verschiedenste Asset-Typen, Meldung an Fundbüro/Ermittlungsbehörden, Sperrung von Authentisierungsmitteln und SIM-Karten als allgemeine Vorgehensweise sowie ein explizit auf 'abhandengekommene Assets' zugeschnittener Prozess. DER.2.1.A6 ist zudem auf Sicherheitsvorfälle allgemein und nicht speziell auf Verlust/Diebstahl ausgerichtet.

### ASST.7.1 — Nicht mehr benötigte Anwendungen
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `APP.6.A13` [Standard] Deinstallation von Software — _APP.6 Allgemeine Software_
  - `SYS.1.9.A15` [Standard] Härtung des Terminalservers — _SYS.1.9 Terminalserver_
  - `SYS.2.1.A16` [Standard] Deaktivierung und Deinstallation nicht benötigter Komponenten und Kennungen — _SYS.2.1 Allgemeiner Client_
  - `SYS.3.2.2.A7` [Standard] Installation von Apps — _SYS.3.2.2 Mobile Device Management (MDM)_
  - `SYS.4.4.A13` [Standard] Deaktivierung und Deinstallation nicht benötigter Komponenten — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.6.A13=0.47, SYS.1.9.A15=0.47, SYS.2.1.A16=0.47, SYS.3.2.2.A7=0.47, SYS.4.4.A13=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9300 gs_ids=APP.6.A13;SYS.2.1.A16;SYS.1.9.A15;SYS.3.2.2.A7;SYS.4.4.A13
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] APP.6.A13 deckt den Kernaspekt der Deinstallation von Software ab, einschließlich dem Entfernen nicht mehr benötigter Dateien und Rückgängigmachen produktbezogener Systemeinträge. SYS.2.1.A16 ergänzt dies für Clients, indem nicht benötigte Anwendungen, Module, Programme, Dienste und Kennungen deinstalliert bzw. deaktiviert oder gelöscht werden sollen. SYS.1.9.A15 trifft ebenfalls den Teilaspekt, dass nicht benötigte Anwendungen auf Terminalservern entfernt werden sollen. SYS.3.2.2.A7 ist relevant, weil dort Apps über MDM installiert, deinstalliert und aktualisiert werden; damit wird der geregelte Deinstallationsprozess für mobile Endgeräte adressiert. SYS.4.4.A13 behandelt schließlich das Deaktivieren oder Deinstallieren nicht benötigter Komponenten auf IoT-Geräten, einschließlich Anwendungen und Dienste. Zusammen überdecken diese Anforderungen den technischen Kern der Entfernung nicht mehr benötigter Anwendungsinstanzen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die GS++-spezifischen Aspekte einer explizit geregelten, nachvollziehbaren Deinstallation aller Anwendungsinstanzen über alle Plattformen hinweg, inklusive expliziter Entfernung zugehöriger Zugriffsrechte und Cloud-Zugänge. Ebenfalls fehlt die Aussage, dass bei nicht kontrollierbaren Cloud-Instanzen stattdessen die dortigen Daten zu löschen sind. Die Kandidaten adressieren vor allem das Entfernen/Deinstallieren von Softwarekomponenten auf bestimmten Zielsystemen, aber nicht den vollständigen End-to-End-Prozess mit Berechtigungsabbau und Cloud-Datenlöschung.

### ASST.7.6 — Autorisierung von Veräußerungen
- **Confidence:** 0.39
- **Gemappte GS-Anforderungen:**
  - `CON.6.A11` [Basis] Löschung und Vernichtung von Datenträgern durch externe Dienstleistende — _CON.6 Löschen und Vernichten_
  - `CON.6.A2` [Basis] Ordnungsgemäßes Löschen und Vernichten von schützenswerten Betriebsmitteln und Informationen — _CON.6 Löschen und Vernichten_
  - `CON.6.A8` [Standard] Erstellung einer Richtlinie für die Löschung und Vernichtung von Informationen — _CON.6 Löschen und Vernichten_
  - `OPS.2.3.A10` [Standard] Etablierung einer zuständigen Person für das Auslagerungsmanagement — _OPS.2.3 Nutzung von Outsourcing_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `SYS.3.1.A7` [Standard] Geregelte Übergabe und Rücknahme eines Laptops — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: CON.6.A11=0.39, CON.6.A2=0.39, CON.6.A8=0.39, OPS.2.3.A10=0.39, ORP.5.A4=0.39, SYS.3.1.A7=0.39
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7800 gs_ids=CON.6.A2;CON.6.A8;CON.6.A11;SYS.3.1.A7;OPS.2.3.A10;ORP.5.A4
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.6.A2, CON.6.A8 und CON.6.A11 decken die Regelung rund um das sichere Löschen/Vernichten vor Entsorgung bzw. bei externer Durchführung ab; SYS.3.1.A7 regelt die sichere Übergabe eines Laptops vor Weitergabe und damit einen konkreten Veräußerungsfall. OPS.2.3.A10 und ORP.5.A4 adressieren die Einbindung zuständiger Personen sowie den Umgang mit vertraglichen/rechtlichen Vorgaben, was einzelne Freigabeaspekte unterstützen kann. Die eigentliche Grundschutz++-Kernforderung "Autorisierung von Veräußerungen" verlangt jedoch einen expliziten Freigabe- bzw. Genehmigungsprozess für die endgültige Abgabe oder Eigentumsübertragung von Assets einschließlich Zuständigkeiten, Entscheidungskriterien und revisionssicherer Autorisierung; genau diese eigenständige Autorisierung von Veräußerungen wird in den Kandidaten nicht vollständig beschrieben.
- **Lücken:** [gpt-5.4-mini] Es fehlt ein expliziter, assetbezogener Veräußerungs-Freigabeprozess vor Verkauf/Spende/Rückgabe/Recycling mit klaren Genehmigungsstufen, Verantwortlichkeiten, Entscheidungskriterien und dokumentierter Autorisierung. Die Kandidaten behandeln vor allem Löschung/Vernichtung, Übergabe einzelner Laptops oder allgemeines Compliance-/Outsourcing-Management, nicht die formale Freigabe endgültiger Asset-Veräußerungen.

### BER.1.1.3 — Bekanntgabe
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A1` [Basis] Erstellung einer Sicherheitsrichtlinie — _NET.3.2 Firewall_
  - `OPS.1.1.3.A11` [Standard] Kontinuierliche Dokumentation der Informationsverarbeitung — _OPS.1.1.3 Patch- und Änderungsmanagement_
  - `OPS.1.1.5.A8` [Standard] Archivierung von Protokollierungsdaten — _OPS.1.1.5 Protokollierung_
  - `OPS.1.2.5.A6` [Standard] Erstellung einer Richtlinie für die Fernwartung — _OPS.1.2.5 Fernwartung_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A1=0.42, OPS.1.1.3.A11=0.42, OPS.1.1.5.A8=0.42, OPS.1.2.5.A6=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=OPS.1.1.5.A8;OPS.1.1.3.A11;OPS.1.2.5.A6;NET.3.2.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung BER.1.1.3 verlangt, dass berechtigte bzw. zuständige Personen oder Rollen über Verfahren und Regelungen informiert werden. Dies wird inhaltlich am ehesten durch OPS.1.2.5.A6 abgedeckt, da dort eine Richtlinie zur Fernwartung erstellt werden soll, die allen Zuständigen bekannt sein muss. Ebenfalls passt NET.3.2.A1, weil die spezifische Sicherheitsrichtlinie allen zuständigen Mitarbeitenden bekannt sein und Grundlage ihrer Arbeit sein muss; das trifft den Informations- und Verbindlichkeitsaspekt gut. OPS.1.1.3.A11 ergänzt dies insofern, als Änderungen dokumentiert und entsprechende Regelungen erarbeitet werden sollen, was die Bekanntgabe von Verfahrensänderungen unterstützt. OPS.1.1.5.A8 trägt nur indirekt bei, da Archivierung von Protokollierungsdaten unter Berücksichtigung gesetzlicher Regelungen zwar Regelungsbezug hat, aber keine Information der zuständigen Personen über Verfahren fordert.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine, bausteinübergreifende Pflicht zur aktiven Bekanntgabe an zuständige Personen oder Rollen, insbesondere die explizite Unterrichtung bei Änderungen sowie die organisatorische Benachrichtigung im Onboarding-Prozess. Die Kandidaten decken eher dokumentations- bzw. richtlinienbezogene Bekanntheit ab, nicht den allgemeinen Kommunikationsprozess für alle Verfahren und Regelungen.

### BER.1.2 — Regelmäßige Überprüfung
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `DER.1.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `DER.1.A13` [Standard] Regelmäßige Audits der Detektionssysteme — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `INF.1.A36` [Standard] Regelmäßige Aktualisierungen der Dokumentation — _INF.1 Allgemeines Gebäude_
  - `OPS.1.1.1.A2` [Basis] Festlegung von Rollen und Berechtigungen für den IT-Betrieb — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `OPS.1.2.2.A2` [Basis] Entwicklung eines Archivierungskonzepts — _OPS.1.2.2 Archivierung_
  - `ORP.5.A8` [Standard] Regelmäßige Überprüfungen des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `SYS.3.2.2.A20` [Basis] Regelmäßige Überprüfung des MDM — _SYS.3.2.2 Mobile Device Management (MDM)_
  - `APP.4.3.A20` [Standard] Regelmäßige Audits — _APP.4.3 Relationale Datenbanken_
  - `OPS.1.2.2.A13` [Standard] Regelmäßige Revision der Archivierungsprozesse — _OPS.1.2.2 Archivierung_
- **Begründung:** Gemittelte Kandidatenscores: DER.1.A1=0.43, DER.1.A13=0.43, INF.1.A36=0.43, OPS.1.1.1.A2=0.43, OPS.1.2.2.A2=0.43, ORP.5.A8=0.43, SYS.3.2.2.A20=0.43, APP.4.3.A20=0.33, OPS.1.2.2.A13=0.33
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=ORP.5.A8;DER.1.A1;DER.1.A13;OPS.1.1.1.A2;INF.1.A36;OPS.1.2.2.A2;SYS.3.2.2.A20
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6600 gs_ids=APP.4.3.A20;OPS.1.2.2.A13
Model-Begründungen:
[gpt-5.4-mini] Mehrere Kandidaten treffen den Kern der Forderung nach regelmäßiger bzw. anlassbezogener Überprüfung von Verfahren/Regelungen auf Aktualität. ORP.5.A8 fordert explizit, das Compliance Management und die daraus folgenden Anforderungen und Maßnahmen regelmäßig auf Effizienz und Effektivität zu überprüfen. OPS.1.1.1.A2 verlangt, Rollen und Berechtigungen regelmäßig zu prüfen und an aktuelle Gegebenheiten anzupassen. OPS.1.2.2.A2 enthält die regelmäßige Anpassung eines Konzeptes an aktuelle Gegebenheiten. INF.1.A36 fordert die regelmäßige Überprüfung und Aktualisierung von Dokumentation. DER.1.A1 und DER.1.A13 verlangen regelmäßige Überprüfungen bzw. Audits von Richtlinien und Detektionssystemen auf korrekte Umsetzung, Aktualität und Wirksamkeit. SYS.3.2.2.A20 fordert ebenfalls regelmäßige Überprüfung von Sicherheitseinstellungen und Berechtigungen. Diese Anforderungen bilden die Grundidee einer planmäßigen Überprüfung und Nachsteuerung ab. Sie decken jedoch nicht vollständig die GS++-Anforderung ab, weil dort ausdrücklich die Überprüfung von Verfahren und Regelungen der Berechtigung einschließlich anlassbezogener Trigger (z. B. Sicherheitsvorfall, strategische Neuausrichtung, neue gesetzliche Anforderungen) im allgemeinen Sinne gefordert wird; die Kandidaten sind teils domänenspezifisch (MDM, Detektion, Archivierung, Dokumentation, Betrieb) und nicht durchgängig auf Berechtigungsverfahren bezogen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine, domänenübergreifende Überprüfung von Berechtigungsverfahren und -regelungen sowie die explizit geforderte anlassbezogene Überprüfung bei Ereignissen wie Sicherheitsvorfällen, strategischer Neuausrichtung oder neuen gesetzlichen Anforderungen. Die vorhandenen Kandidaten liefern eher Beispiele für regelmäßige Reviews in einzelnen Fachdomänen.

### BER.3.15 — Keine Gruppenkonten
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `NET.3.4.A10` [Standard] Sichere Nutzung von Identitäten — _NET.3.4 Network Access Control_
  - `OPS.1.1.2.A22` [Basis] Trennung von administrativen und anderen Tätigkeiten — _OPS.1.1.2 Ordnungsgemäße IT-Administration_
  - `SYS.2.4.A3` [Basis] Verwendung geeigneter Konten — _SYS.2.4 Clients unter macOS_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.4.A10=0.44, OPS.1.1.2.A22=0.44, SYS.2.4.A3=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=OPS.1.1.2.A22;SYS.2.4.A3;NET.3.4.A10
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.2.A22 passt inhaltlich, weil dort gefordert wird, dass Zugangskennungen für IT-Administration sich von anderen Zugangskennungen unterscheiden sollen; das adressiert die Trennung von Konten, aber nicht ausdrücklich das Verbot von Gruppenkonten. SYS.2.4.A3 passt teilweise, weil für die Nutzung durch mehrere Benutzende jeweils eigene Konten gefordert werden und das Gast-Konto zu deaktivieren ist; das deckt die Idee individueller Konten ab, aber nicht generell Gruppenkonten in Berechtigungen. NET.3.4.A10 ist nur eingeschränkt passend, weil dort individuelle Identitäten für die NAC-Authentisierung gefordert werden und Identitäten, die von mehr als einem Endgerät verwendet werden, nur ausnahmsweise zulässig sind; das betrifft Identitäten im NAC-Kontext, nicht allgemein Gruppenkonten. Insgesamt wird der Kern der Anforderung – keine gemeinsam genutzten Zugangskonten zur eindeutigen Nachvollziehbarkeit von Handlungen – nur teilweise abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist das allgemeine, berechtigungsweite Verbot von Gruppenkonten für alle Zugangskonten und die explizite Zielsetzung der eindeutigen Zuordenbarkeit von Tätigkeiten. Die Kandidaten beziehen sich nur auf Teilkontexte (IT-Administration, macOS-Mehrbenutzerbetrieb, NAC-Authentisierung) und formulieren kein generelles Verbot gemeinsam genutzter Konten.

### BER.6.8 — Kriterien für die Qualität von Passwörtern
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `CON.1.A10` [Standard] Erstellung eines Kryptokonzepts — _CON.1 Kryptokonzept_
  - `CON.1.A9` [Standard] Festlegung von Kriterien für die Auswahl von Hard- oder Software mit kryptografischen Funktionen — _CON.1 Kryptokonzept_
  - `CON.10.A16` [Standard] Mehr-Faktor-Authentisierung — _CON.10 Entwicklung von Webanwendungen_
  - `OPS.1.2.5.A17` [Standard] Authentisierungsmechanismen bei der Fernwartung — _OPS.1.2.5 Fernwartung_
  - `ORP.4.A10` [Standard] Schutz von Benutzendenkennungen mit weitreichenden Berechtigungen — _ORP.4 Identitäts- und Berechtigungsmanagement_
  - `ORP.4.A23` [Basis] Regelung für passwortverarbeitende Anwendungen und IT-Systeme — _ORP.4 Identitäts- und Berechtigungsmanagement_
- **Begründung:** Gemittelte Kandidatenscores: CON.1.A10=0.43, CON.1.A9=0.43, CON.10.A16=0.43, OPS.1.2.5.A17=0.43, ORP.4.A10=0.43, ORP.4.A23=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=ORP.4.A23;CON.1.A10;CON.1.A9;ORP.4.A10;CON.10.A16;OPS.1.2.5.A17
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung BER.6.8 fordert, Kriterien für die Qualität von Passwörtern anhand von Lebensdauer und Angriffsmöglichkeiten zu verankern. Von den Kandidaten adressiert ORP.4.A23 nur Teilaspekte des Passwortumgangs (u. a. ausreichend starke Passwörter, Passwortwechsel, sichere Speicherung und Übertragung), aber keine explizite Festlegung von Qualitätskriterien nach Lebensdauer oder Angriffsszenarien. ORP.4.A10 und OPS.1.2.5.A17 behandeln Mehr-Faktor-Authentisierung für privilegierte Konten bzw. Fernwartung; CON.10.A16 fordert MFA in Webanwendungen. Diese Maßnahmen beeinflussen zwar die erforderliche Passwortqualität im Sinne der Guidance, regeln aber nicht selbst Kriterien für die Passwortqualität. CON.1.A10 und CON.1.A9 betreffen die Auswahl bzw. das Kryptokonzept für kryptografische Funktionen und sind damit nur indirekt relevant, da die Guidance BSI TR-02102 erwähnt, jedoch keine Passwortqualitätskriterien festlegt. Daher liegt nur eine teilweise inhaltliche Überschneidung vor.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die eigentlichen, expliziten Kriterien zur Passwortqualität selbst: etwa Mindestentropie, konkrete Passwortlängen, Differenzierung nach Lebensdauer/Nutzungsdauer, Anpassung an Angriffsmöglichkeiten (z. B. Anzahl der Login-Versuche, Schutzmaßnahmen, Anwendungskontext) sowie die Möglichkeit, diese Kriterien einmalig oder pro Anwendung/Zugang zu differenzieren.

### BER.7.16.3 — Erneuerung
- **Confidence:** 0.36
- **Gemappte GS-Anforderungen:**
  - `APP.3.6.A17` [Standard] Einsatz von DNSSEC — _APP.3.6 DNS-Server_
  - `CON.1.A4` [Basis] Geeignetes Schlüsselmanagement — _CON.1 Kryptokonzept_
  - `DER.2.3.A4` [Basis] Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln — _DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle_
- **Begründung:** Gemittelte Kandidatenscores: APP.3.6.A17=0.36, CON.1.A4=0.36, DER.2.3.A4=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7200 gs_ids=CON.1.A4;DER.2.3.A4;APP.3.6.A17
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.1.A4 deckt den allgemeinen Teil des Schlüsselmanagements ab, insbesondere dass Integrität und Authentizität von Schlüsseln sichergestellt werden müssen und dass zeitlich befristete Zertifikate/Schlüssel rechtzeitig erneuert werden. DER.2.3.A4 passt, weil dort bei kompromittierten TLS-Schlüsseln bzw. einer kompromittierten CA die erneute Erzeugung, Verteilung sowie das Sperren/Rückrufen der betroffenen Schlüssel und Zertifikate gefordert wird. APP.3.6.A17 ist ein fachlich enger Treffer für die regelmäßige Erneuerung von DNSSEC-Schlüsseln (KSK/ZSK), behandelt aber nur den speziellen DNSSEC-Anwendungsfall. Zusammen adressieren die Kandidaten die Erneuerung und Absicherung von Schlüsseln bzw. Zertifikaten, jedoch nicht den spezifischen Prüfmechanismus der GS++-Anforderung, also das Testen des Schlüssels anhand der Vorgaben für die Schlüsselbeglaubigung bei einer Erneuerung einer Beglaubigung.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkreten Vorgaben zur Schlüsselbeglaubigungs-Erneuerung, insbesondere die explizite Schlüsselprüfung im Rahmen der Zertifikatserneuerung (z. B. Signaturverifikation, Fingerprint-Abgleich, Validierung gegen Sperrlisten) als eigenständige Anforderung. Auch die Aussage, dass Berechtigung den Schlüssel bei Erneuerung einer Beglaubigung testen soll, wird nur indirekt über allgemeine Integritäts-/Authentizitäts- bzw. Erneuerungsvorgaben berührt.

## Keine Abdeckung (2)

### BER.2.5 — Deaktivierung bei Weggang
- **Confidence:** 0.48
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9700 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidaten beschreibt inhaltlich die Deaktivierung der zugeordneten Identität bei Weggang von Nutzenden. Die Vorschläge behandeln andere Themen wie Protokollierung, Outsourcing-Beendigung, Aussonderung, Audits oder allgemeine Personalmaßnahmen, aber nicht das Sperren/Deaktivieren von Benutzerkonten bzw. Identitäten als Berechtigungsmaßnahme.
- **Lücken:** [gpt-5.4-mini] Es fehlt eine klassische Grundschutz-Anforderung zur Sperrung, Deaktivierung oder Löschung von Benutzerkonten/Identitäten bei Ausscheiden oder längerfristiger Abwesenheit von Nutzenden.

### BER.7.16.6 — Revocationstatus
- **Confidence:** 0.49
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9800 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidatenanforderungen deckt die GS++-Anforderung BER.7.16.6 inhaltlich ab. Gefordert ist die Dokumentation des Revocationstatus eines öffentlichen Schlüssels im Verzeichnis öffentlicher Schlüssel, also die Pflege/Erfassung des Sperr- bzw. Widerrufsstatus von Schlüsseln. Die Kandidaten CON.1.A4, CON.1.A5, DER.2.3.A4 und CON.1.A2 behandeln zwar allgemein Schlüsselmanagement, Löschen/Vernichten, Sperren/Rückrufen nach Kompromittierung oder Aufbewahrung in Backups, aber keine dokumentierte Statusführung im Schlüsselverzeichnis. Auch die übrigen Kandidaten betreffen andere Domänen (Gebäude-, Protokollierungs-, AD-, WLAN-, E-Mail-, Container- oder Fernwartungsaspekte) und passen nicht.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt ist die konkrete Pflicht, den Revocationstatus im Verzeichnis öffentlicher Schlüssel zu dokumentieren bzw. als Metadatum zu führen. Allgemeine Aussagen zu gesperrten/zurückgerufenen Schlüsseln oder deren sicherer Löschung reichen dafür nicht aus.
