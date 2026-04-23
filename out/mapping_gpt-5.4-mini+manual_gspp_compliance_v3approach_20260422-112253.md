# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T11:22:53

**Gesamt:** 20 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 19 |
| Keine Abdeckung | 1 |

## Teilweise abgedeckt (19)

### ARCH.1.1.1 — Dokumentation
- **Confidence:** 0.42
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
  - `ORP.2.A1` [Basis] Geregelte Einarbeitung neuer Mitarbeitender — _ORP.2 Personal_
  - `SYS.1.1.A11` [Standard] Festlegung einer Sicherheitsrichtlinie für Server — _SYS.1.1 Allgemeiner Server_
  - `SYS.4.4.A6` [Standard] Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.2.1.A1=0.42, APP.6.A10=0.42, APP.7.A6=0.42, CON.10.A11=0.42, CON.8.A12=0.42, DER.3.1.A6=0.42, DER.4.A12=0.42, IND.1.A11=0.42, IND.2.7.A1=0.42, NET.1.2.A12=0.42, ORP.2.A1=0.42, SYS.1.1.A11=0.42, SYS.4.4.A6=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=APP.6.A10;DER.4.A12;NET.1.2.A12;CON.8.A12;APP.2.1.A1;SYS.1.1.A11;SYS.4.4.A6;CON.10.A11;APP.7.A6;IND.1.A11;IND.2.7.A1;DER.3.1.A6;ORP.2.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Anforderungen APP.6.A10, SYS.1.1.A11, SYS.4.4.A6 und APP.2.1.A1 verlangen jeweils, Regelungen in einer Sicherheitsrichtlinie festzuhalten; CON.8.A12, CON.10.A11, APP.7.A6, NET.1.2.A12, IND.1.A11 und IND.2.7.A1 verlangen eine Dokumentation von Architektur-, Betriebs-, Entwicklungs-, Netzmanagement- bzw. System-/OT-Aspekten sowie Rollen und Zuständigkeiten; DER.4.A12 und DER.3.1.A6 behandeln die Dokumentation von Prozessen, Entscheidungen und Bewertungsschemata; ORP.2.A1 verlangt, Mitarbeitende über Regelungen, Handlungsanweisungen und Verfahrensweisen zu informieren. Zusammen decken diese Anforderungen den Dokumentationsgedanken der GS++-Anforderung in weiten Teilen ab. Sie adressieren jedoch nicht vollständig die spezifische Pflicht, die Verfahren und Regelungen der Architektur als verbindliche, zielgruppenorientierte Dokumentation der Architektur selbst zu dokumentieren.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die explizite architekturspezifische Dokumentation von Verfahren und Regelungen als Teil der Architektur-Governance, insbesondere die Ausrichtung der Dokumentation an Management- und Umsetzungsrollen sowie der generische Charakter einer übergreifenden, verbindlichen Regelungsdokumentation für die gesamte Architektur.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.80
- **Gemappte GS-Anforderungen:**
  - `NET.1.1.A11` [Basis] Absicherung eingehender Kommunikation vom Internet in das interne Netz — _NET.1.1 Netzarchitektur und -design_
  - `CON.7.A7` [Basis] Sicherer Remote-Zugriff auf das Netz der Institution — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `CON.7.A8` [Basis] Sichere Nutzung von öffentlichen WLANs — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `NET.3.3.A11` [Standard] Sichere Anbindung eines externen Netzes — _NET.3.3 VPN_
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A11=0.80, CON.7.A7=0.44, CON.7.A8=0.44, NET.3.3.A11=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=CON.7.A7;CON.7.A8;NET.1.1.A11
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] CON.7.A7 adressiert den sicheren Fernzugriff über VPN für mobile bzw. externe Zugriffe und damit einen Teil des Umgangs mit externen Netzanschlüssen. CON.7.A8 ergänzt dies für öffentliche WLANs, indem für den Zugriff auf das Netz der Institution VPN oder vergleichbare Sicherheitsmechanismen gefordert werden. NET.1.1.A11 deckt den eingangsseitigen, IP-basierten Zugriff aus dem Internet ins interne Netz über sichere Kommunikationskanäle und die Beschränkung auf vertrauenswürdige Systeme ab. Gemeinsam passen diese Anforderungen zur Zielrichtung der GS++-Anforderung, externe Zugänge zu kontrollieren und abzusichern.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der allgemeine architektonische Grundsatz, Verbindungen über externe Netzanschlüsse insgesamt zu minimieren bzw. zu beschränken. Insbesondere fehlt in den Kandidaten eine allgemeine Vorgabe zur Einschränkung aller externen Netzanschlüsse als Architekturprinzip; die vorhandenen Anforderungen fokussieren vor allem auf sicheren Fernzugriff, VPN-Nutzung und eingehende Internetzugriffe.

### ARCH.2.2.11 — Physische Segmentierung
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `INF.14.A28` [Hoch] Physische Trennung der GA — _INF.14 Gebäudeautomation_
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A32` [Hoch] Physische Trennung von Management-Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.2.A32` [Hoch] Physische Trennung des Managementnetzes — _NET.1.2 Netzmanagement_
  - `SYS.1.5.A15` [Standard] Betrieb von Gast-Betriebssystemen mit unterschiedlichem Schutzbedarf — _SYS.1.5 Virtualisierung_
  - `SYS.1.5.A4` [Basis] Sichere Konfiguration eines Netzes für virtuelle Infrastrukturen — _SYS.1.5 Virtualisierung_
  - `SYS.1.8.A15` [Standard] Sichere Trennung von Mandanten in Speicherlösungen — _SYS.1.8 Speicherlösungen_
  - `SYS.2.5.A2` [Basis] Planung der verwendeten Netze für virtuelle Clients — _SYS.2.5 Client-Virtualisierung_
  - `NET.1.1.A22` [Standard] Spezifikation des Segmentierungskonzepts — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A23` [Standard] Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A31` [Hoch] Physische Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A33` [Hoch] Mikrosegmentierung des Netzes — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A28=0.45, INF.14.A6=0.45, NET.1.1.A32=0.45, NET.1.1.A4=0.45, NET.1.2.A32=0.45, SYS.1.5.A15=0.45, SYS.1.5.A4=0.45, SYS.1.8.A15=0.45, SYS.2.5.A2=0.45, NET.1.1.A22=0.34, NET.1.1.A23=0.34, NET.1.1.A31=0.34, NET.1.1.A33=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9000 gs_ids=NET.1.1.A32;NET.1.2.A32;INF.14.A28;NET.1.1.A4;INF.14.A6;SYS.1.5.A4;SYS.2.5.A2;SYS.1.5.A15;SYS.1.8.A15
[manual:gspp_compliance_v3approach] coverage=teilweise confidence=0.6711 gs_ids=NET.1.1.A31;NET.1.1.A23;NET.1.1.A33;NET.1.1.A22
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.11 fordert physische Segmentierung bzw. die Einschränkung von Verbindungen zwischen Segmenten auf physischer Ebene, um Umgehungen der Netztrennung durch virtuelle oder rein logische Trennung zu vermeiden. Dies wird inhaltlich durch NET.1.1.A32 und NET.1.2.A32 direkt aufgegriffen, da beide die physische Trennung von Management-Segmenten bzw. des Managementnetzes verlangen. Ebenfalls passend sind INF.14.A28 und INF.14.A6, weil sie physische bzw. mindestens logische Trennung von GA-Netzen sowie die Nutzung separierter Zonen und kontrollierter Übergänge behandeln. NET.1.1.A4 deckt die physische Separierung von Zonen im Gesamtnetz und die Absicherung der Übergänge durch Firewalls ab, also die relevante Segmentierung der Netzinfrastruktur. SYS.1.5.A4 und SYS.2.5.A2 sind ebenfalls relevant, da sie ausdrücklich verhindern, dass Netztrennung über virtuelle Netze bzw. virtuelle Clients umgangen wird; das adressiert den zweiten Kernaspekt der GS++-Guidance, ersetzt aber keine echte physische Segmentierung. SYS.1.5.A15 und SYS.1.8.A15 behandeln Isolation bzw. Netzsegmentierung in Virtualisierungs- und Speicherumgebungen und stützen damit ebenfalls den Schutzgedanken gegen Umgehung von Segmentierung. Trotzdem bleibt die GS++-Anforderung weiter gefasst: sie zielt allgemein auf physische Segmentierung von Netzarchitekturen, nicht nur auf einzelne Sonderdomänen wie Management, GA, Virtualisierung oder Storage.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die allgemeine, domänenübergreifende Forderung nach physischer Segmentierung beliebiger Netzsegmente. Die Kandidaten adressieren vor allem Management-Netze, GA-Netze, Virtualisierung und Speicherlösungen sowie die Verhinderung virtueller Umgehung, aber keine generische, für alle Segmenttypen geltende physische Trennung als Architekturprinzip.

### ARCH.2.2.8 — Segmentierung von Test und Betrieb
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.6.A13` [Standard] Trennung der Testumgebung von der Produktivumgebung — _OPS.1.1.6 Software-Tests und -Freigaben_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.6.A13=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9400 gs_ids=OPS.1.1.6.A13
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.6.A13 trifft den Kern der GS++-Anforderung unmittelbar: Es fordert, dass Software in einer vorgesehenen Testumgebung getestet wird und dass diese Testumgebung von der Produktivumgebung getrennt betrieben wird. Damit ist die geforderte Segmentierung bzw. Trennung von Test und Betrieb inhaltlich abgedeckt. Die ergänzenden Hinweise zu Dokumentation und Verfahren nach Testende ändern nichts am wesentlichen Match zur geforderten Einschränkung von Verbindungen bzw. Trennung zwischen Test- und Betriebsumgebung.
- **Lücken:** [gpt-5.4-mini] Keine wesentlichen Lücken gegenüber der GS++-Anforderung erkennbar; die Anforderung zielt hier primär auf die Trennung von Test- und Produktivumgebung, nicht spezifisch auf Netze im engeren Sinn.

### ARCH.2.2.9 — Segmentierung von IPv4 und IPv6
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A20` [Standard] Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A17` [Standard] Deaktivierung von IPv4 oder IPv6 — _NET.3.2 Firewall_
  - `NET.4.2.A16` [Hoch] Trennung des Daten- und VoIP-Netzes — _NET.4.2 VoIP_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.43, NET.1.1.A20=0.43, NET.3.2.A17=0.43, NET.4.2.A16=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=NET.1.1.A20;NET.3.2.A17;NET.4.2.A16;INF.14.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.1.1.A20 passt inhaltlich, weil die Zuweisung dedizierter Subnetze für IPv4-/IPv6-Endgerätegruppen eine Segmentierung nach Protokoll vorsieht. NET.3.2.A17 unterstützt die Trennung zusätzlich, indem ungenutztes IPv4 oder IPv6 an Netzsegment-Grenzen deaktiviert werden soll; das reduziert Übergänge zwischen IPv4- und IPv6-Teilnetzen. NET.4.2.A16 ist nur indirekt passend, da dort zwar eine Trennung von VoIP- und Datennetz gefordert wird, aber nicht speziell IPv4 gegen IPv6; daher höchstens als allgemeines Segmentierungsprinzip verwertbar. INF.14.A6 ist ebenfalls nur teilweise passend, weil es die kontrollierte Trennung von GA-Netzen und anderen Netzen fordert, jedoch keine spezifische IPv4-/IPv6-Segmentierung beschreibt. Insgesamt wird die Zielrichtung der Protokolltrennung adressiert, aber nicht vollständig: Die GS++-Anforderung verlangt explizit die Einschränkung von Verbindungen zwischen IPv4 und IPv6 im gesamten Architekturkontext, während die Kandidaten eher Subnetzzuordnung, Protokoll-Deaktivierung oder domänenspezifische Segmentierung behandeln.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die explizite, generelle Einschränkung von Verbindungen zwischen IPv4 und IPv6 sowie die architekturweite Vorgabe für alle betroffenen Segmente. Die Kandidaten behandeln vor allem Subnetzzuordnung, Abschaltung nicht benötigter Protokolle oder andere Domänen (VoIP/GA), aber keine klare, umfassende IPv4-vs.-IPv6-Verbindungsbeschränkung.

### ARCH.5.1.12 — Software-definierte Verbindungen
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A2` [Basis] Festlegen der Firewall-Regeln — _NET.3.2 Firewall_
  - `SYS.3.1.A3` [Basis] Einsatz von Personal Firewalls — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A2=0.42, SYS.3.1.A3=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=NET.3.2.A2;SYS.3.1.A3
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A2 passt inhaltlich teilweise, weil dort für Firewalls eindeutige Regeln für zugelassene Kommunikationsverbindungen gefordert werden und nicht erlaubte Verbindungen unterbunden werden müssen. Das deckt den Grundgedanken der Verbindungssteuerung ab, aber nur statisch auf Basis fest definierter Regeln. SYS.3.1.A3 passt ebenfalls teilweise, da Personal Firewalls mit restriktiven Filterregeln eingesetzt werden sollen; auch das ist eine technische Verbindungsbegrenzung. Beide Anforderungen enthalten jedoch keine dynamische, kontextabhängige Bewertung aktueller Merkmale wie Geräteintegrität, Standort, Auslastung oder zeitliche Rahmenbedingungen. Genau diese dynamische Kriterienbasis ist der Kern von ARCH.5.1.12, daher nur Teildeckung.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die wesentlichen GS++-Aspekte der dynamischen/kontextabhängigen Entscheidung über Verbindungen, etwa adaptive Policies, Context Attributes, Device Posture, Risikobewertung oder andere situativ ermittelte Merkmale. Abgedeckt ist nur die statische Allowlist-/Filterregelung, nicht software-definierte oder kontextsensitiv gesteuerte Verbindungen.

### ARCH.5.1.8 — Inspektion verschlüsselter Verbindungen
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A21` [Standard] Temporäre Entschlüsselung des Datenverkehrs — _NET.3.2 Firewall_
  - `NET.3.2.A28` [Hoch] Zentrale Filterung von aktiven Inhalten — _NET.3.2 Firewall_
  - `NET.1.1.A12` [Basis] Absicherung ausgehender interner Kommunikation zum Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A20` [Standard] Absicherung von grundlegenden Internetprotokollen — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A21=0.45, NET.3.2.A28=0.45, NET.1.1.A12=0.34, NET.3.2.A20=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=NET.3.2.A28;NET.3.2.A21
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6855 gs_ids=NET.3.2.A20;NET.1.1.A12
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A28 deckt die zentrale Filterung aktiver Inhalte durch Sicherheitsproxies ab und nennt ausdrücklich die Entschlüsselung verschlüsselten Datenverkehrs als Voraussetzung. NET.3.2.A21 passt ebenfalls inhaltlich, weil es die temporäre Entschlüsselung verschlüsselter Verbindungen in nicht vertrauenswürdige Netze zur Protokollverifikation und Schadsoftwareprüfung fordert. Beide Anforderungen adressieren damit die Inspektion verschlüsselter Verbindungen auf Netzwerkebene. Die GS++-Anforderung ist jedoch breiter, weil sie die Architektur für externe Netzanschlüsse allgemein auf die Inhaltsinspektion un- und verschlüsselter Verbindungen nach Inhaltsart ausrichtet; die Kandidaten fokussieren auf aktive Inhalte bzw. Malwareprüfung und beschreiben nicht die allgemeine, inhaltsabhängige Einschränkung aller Verbindungen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeinere architekturelle Vorgabe für externe Netzanschlüsse sowie die explizite Inhaltssteuerung basierend auf der Art des Inhalts über unverschlüsselte und verschlüsselte Verbindungen hinaus. NET.3.2.A21 bezieht sich zudem nur auf temporäre Entschlüsselung in nicht vertrauenswürdige Netze und auf Protokoll-/Malwareprüfung, nicht auf jede Form von Inhaltsinspektion.

### ASST.2.1.1 — Informationsverantwortung
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `ORP.1.A2` [Basis] Zuweisung der Zuständigkeiten — _ORP.1 Organisation_
- **Begründung:** Gemittelte Kandidatenscores: ORP.1.A2=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9500 gs_ids=ORP.1.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.1.A2 deckt die wesentliche Aussage der GS++-Anforderung direkt ab: Für alle Geschäftsprozesse, Anwendungen, IT-Systeme, Räume/Gebäude und Kommunikationsverbindungen muss festgelegt werden, wer zuständig ist, und die Mitarbeitenden müssen darüber informiert sein. Das entspricht inhaltlich der geforderten Zuweisung der Zuständigkeit für die Verarbeitung von Informationen und Assets sowie der Klarstellung der internen Verantwortlichkeit (Asset Ownership).

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
[gpt-5.4-mini] OPS.1.1.1.A6 passt inhaltlich am besten, weil die Anforderung zum IT-Asset-Management eine Übersicht aller vorhandenen IT-Assets, deren regelmäßige Prüfung und Aktualisierung verlangt. Das deckt den organisatorischen Kern des Aufdeckens unbekannter bzw. nicht autorisierter Systeme teilweise ab. OPS.3.2.A14 ergänzt dies durch die kontinuierliche Überwachung der eingesetzten Prozesse, Anwendungen und IT-Systeme, was ebenfalls zur Erkennung auffälliger oder unbekannter Systeme beitragen kann. Beide Anforderungen zielen jedoch nicht spezifisch auf das aktive oder passive Auffinden unautorisierter IT-Systeme im Netz ab.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkreten Erkennungsverfahren und Maßnahmen der GS++-Anforderung, insbesondere aktive Netzscans, passive Verkehrsanalyse, WLAN-Erkennung unbekannter Access Points sowie das anschließende Behandeln gefundener Systeme durch Quarantäne, Entfernung oder nachträgliche Autorisierung. Die Domain-Netzwerkerkennung ist daher nur indirekt bzw. organisatorisch erfasst.

### ASST.4.4 — Nachweis des Zugangs
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `DER.3.1.A27` [Standard] Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen — _DER.3.1 Audits und Revisionen_
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.3.2.A6` [Basis] Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.3.2 Anbieten von Outsourcing_
- **Begründung:** Gemittelte Kandidatenscores: DER.3.1.A27=0.44, OPS.2.3.A7=0.44, OPS.3.2.A6=0.44
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=DER.3.1.A27;OPS.3.2.A6;OPS.2.3.A7
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.3.1.A27 deckt den Aspekt der nachvollziehbaren, revisionssicheren Aufbewahrung von Unterlagen zu Audits und Revisionen ab, was dem geforderten manipulationssicheren Nachweis- und Archivierungscharakter teilweise entspricht. OPS.3.2.A6 und OPS.2.3.A7 enthalten Regelungen zur dokumentierten Rückgabe von Informationen/Daten sowie zur Prüfung des Entzugs von Zugangs-, Zutritts- und Zugriffsrechten im Outsourcing-Kontext. Damit wird die organisatorische Dokumentation von Übergaben und Nachweisen berührt, jedoch nicht der eigentliche Zugangsnachweis für Nachrichten an einen Empfänger. Wesentliche Aspekte der GS++-Anforderung fehlen: die protokollierte Bestätigung, dass eine konkrete Nachricht ihren Empfänger tatsächlich erreicht hat, die Bindung an Nachrichteninhalt/Versand- und Zieladressen sowie der explizite Fokus auf Streitfall-, Fristen- oder Rechtswirksamkeitsnachweis.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind der eigentliche Zugangsnachweis für einzelne Nachrichten, die Bestätigung des tatsächlichen Empfangs durch den Adressaten, die protokollierte Verknüpfung mit konkreten Nachrichteninhalten sowie typische technische Umsetzungen wie Empfangsbestätigungen oder Portal-/Systemprotokolle speziell für den Nachrichtenzugang. Die Kandidaten betreffen eher Aufbewahrung, Rückgabe und Rechteentzug als einen rechtsverbindlichen Zugangsbeleg.

### ASST.6.1 — Abhandenkommen
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `DER.2.1.A7` [Standard] Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `SYS.3.1.A12` [Standard] Verlustmeldung für Laptops — _SYS.3.1 Laptops_
  - `SYS.3.3.A2` [Basis] Sperrmaßnahmen bei Verlust eines Mobiltelefons — _SYS.3.3 Mobiltelefon_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.1.A7=0.46, SYS.3.1.A12=0.46, SYS.3.3.A2=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9100 gs_ids=DER.2.1.A7;SYS.3.1.A12;SYS.3.3.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.2.1.A7 passt, weil die GS++-Anforderung eine Vorgehensweise für den Umgang mit dem Ereignis 'Abhandenkommen von Assets' fordert und damit organisatorisch sehr nahe an einer definierten Behandlung von Sicherheitsvorfällen liegt. SYS.3.1.A12 passt für den speziellen Fall verlorener oder gestohlener Laptops, weil dort Meldewege, Reaktion auf Wiederauftauchen und Neuinstallation gefordert werden. SYS.3.3.A2 passt für den Verlust eines Mobiltelefons, weil SIM-Sperrung und ggf. Fernlöschung/-sperrung als Sofortmaßnahmen genannt werden. Zusammen decken die Kandidaten wesentliche Reaktionsmaßnahmen bei Verlust einzelner Asset-Typen und die generelle Vorfallsbehandlung ab.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind eine allgemeine, asset-übergreifende Verlustprozess-Vorgehensweise für beliebige Informationswerte und Assets sowie ausdrücklich genannte Aspekte wie Fundbüro/Ermittlungsbehörden, systematische Zuständigkeits- und Eskalationsregeln für alle Asset-Klassen und die umfassende Behandlung weiterer verlorener Assets wie Papierdokumente oder sonstige Datenträger.

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
[gpt-5.4-mini] coverage=teilweise confidence=0.9000 gs_ids=APP.6.A13;SYS.2.1.A16;SYS.1.9.A15;SYS.4.4.A13;SYS.3.2.2.A7
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] APP.6.A13 passt inhaltlich, weil es die Deinstallation von Software sowie das Entfernen nicht mehr benötigter Dateien und Systemeinträge behandelt. SYS.2.1.A16 und SYS.4.4.A13 passen ebenfalls, da sie die Deaktivierung bzw. Deinstallation nicht benötigter Anwendungen/Komponenten auf Clients bzw. IoT-Geräten regeln. SYS.1.9.A15 deckt das Entfernen nicht benötigter Anwendungen auf Terminalservern ab. SYS.3.2.2.A7 ist relevant, weil Apps über MDM installiert, deinstalliert und aktualisiert werden sollen, also auch eine geregelte Deinstallation unterstützt wird. Zusammen adressieren die Anforderungen die technische Entfernung nicht mehr benötigter Anwendungen, jedoch nicht alle Aspekte der GS++-Anforderung.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind insbesondere die explizite Verankerung als institutionelle Regelung für alle Anwendungsinstanzen, die vollständige Entfernung zugehöriger Konfigurationen, temporärer Daten und Zugriffsrechte, sowie die Cloud-spezifische Anforderung, wenn die Instanz nicht unter Kontrolle der Institution steht, stattdessen alle dortigen Daten zu löschen. Die organisatorische Steuerung und Nachvollziehbarkeit des gesamten Deinstallationsprozesses wird nur teilweise abgebildet.

### ASST.7.6 — Autorisierung von Veräußerungen
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `CON.6.A1` [Basis] Regelung für die Löschung und Vernichtung von Informationen — _CON.6 Löschen und Vernichten_
  - `CON.6.A2` [Basis] Ordnungsgemäßes Löschen und Vernichten von schützenswerten Betriebsmitteln und Informationen — _CON.6 Löschen und Vernichten_
  - `CON.6.A8` [Standard] Erstellung einer Richtlinie für die Löschung und Vernichtung von Informationen — _CON.6 Löschen und Vernichten_
  - `OPS.1.1.6.A4` [Basis] Freigabe der Software — _OPS.1.1.6 Software-Tests und -Freigaben_
  - `SYS.3.1.A7` [Standard] Geregelte Übergabe und Rücknahme eines Laptops — _SYS.3.1 Laptops_
- **Begründung:** Gemittelte Kandidatenscores: CON.6.A1=0.42, CON.6.A2=0.42, CON.6.A8=0.42, OPS.1.1.6.A4=0.42, SYS.3.1.A7=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=CON.6.A1;CON.6.A2;CON.6.A8;OPS.1.1.6.A4;SYS.3.1.A7
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.6.A1, CON.6.A2 und CON.6.A8 decken den Teilaspekt ab, dass vor dem Entsorgen/Löschen von Informationen und Datenträgern feste Regeln, Zuständigkeiten und eine dokumentierte Richtlinie existieren sollen. SYS.3.1.A7 passt zusätzlich für die sichere Übergabe eines Laptops vor Weitergabe und fordert, schützenswerte Daten vor der Weitergabe zu löschen. OPS.1.1.6.A4 behandelt zwar eine formale Freigabe, aber nur für Software nach Tests und nicht für die Veräußerung von Assets; die inhaltliche Übereinstimmung ist daher nur sehr begrenzt und reicht allein nicht als echter Match für die Veräußerung von Assets. Die GS++-Anforderung ASST.7.6 verlangt jedoch explizit eine Autorisierung von Veräußerungen von Assets als organisatorischen Freigabeprozess für endgültige Abgabe/Eigentumsübertragung. Dieser spezifische Autorisierungs- und Freigabeaspekt für Veräußerungen wird durch die Kandidaten nicht vollständig abgebildet.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind der explizite Freigabe-/Autorisierungsprozess für die Veräußerung als solche, die Entscheidung nach Schutzbedarf/Klassifizierung, die Berücksichtigung von Lizenz-/Vertragsrestriktionen sowie die revisionssichere Protokollierung des Veräußerungsantrags und der Freigabe. Die vorhandenen Treffer beziehen sich überwiegend auf Löschung/Vernichtung bzw. Weitergabe einzelner Geräte, nicht auf die formale Autorisierung von Eigentumsübertragungen oder endgültigen Abgaben von Assets.

### BER.1.1.3 — Bekanntgabe
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `CON.8.A1` [Standard] Definition von Rollen und Zuständigkeiten — _CON.8 Software-Entwicklung_
  - `OPS.1.1.3.A11` [Standard] Kontinuierliche Dokumentation der Informationsverarbeitung — _OPS.1.1.3 Patch- und Änderungsmanagement_
  - `OPS.1.2.5.A6` [Standard] Erstellung einer Richtlinie für die Fernwartung — _OPS.1.2.5 Fernwartung_
- **Begründung:** Gemittelte Kandidatenscores: CON.8.A1=0.42, OPS.1.1.3.A11=0.42, OPS.1.2.5.A6=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=OPS.1.2.5.A6;OPS.1.1.3.A11;CON.8.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.2.5.A6 passt inhaltlich am besten, weil die Anforderung verlangt, dass eine Richtlinie mit den relevanten Regelungen erstellt und allen Zuständigen bekannt gemacht wird. Das deckt den Aspekt der Bekanntgabe von Verfahren und Regelungen an zuständige Personen teilweise ab. OPS.1.1.3.A11 ergänzt dies durch die Forderung, Änderungen in allen Phasen zu dokumentieren und entsprechende Regelungen zu erarbeiten; damit wird der Regelungs- und Dokumentationsaspekt adressiert, nicht aber explizit die Information der zuständigen Rollen. CON.8.A1 ist nur insofern passend, als Rollen und Zuständigkeiten festgelegt werden sollen; die eigentliche Pflicht zur Information dieser Rollen über Verfahren und Regelungen wird jedoch nicht ausdrücklich gefordert. Zusammen decken die Kandidaten den organisatorischen Teil der Bekanntgabe an Zuständige nur teilweise ab.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt ist die explizite Verpflichtung, zuständige Personen oder Rollen aktiv über Verfahren und Regelungen zu informieren, insbesondere anlassbezogen bei Änderungen bzw. automatisiert bei Anpassungen. Ebenfalls fehlt die klare Onboarding- bzw. Änderungsbenachrichtigungslogik. Die Kandidaten behandeln eher Dokumentation, Festlegung und Bekanntheit von Regelungen, aber nicht die verbindliche Kommunikationspflicht.

### BER.1.2 — Regelmäßige Überprüfung
- **Confidence:** 0.44
- **Gemappte GS-Anforderungen:**
  - `DER.1.A1` [Basis] Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `DER.1.A13` [Standard] Regelmäßige Audits der Detektionssysteme — _DER.1 Detektion von sicherheitsrelevanten Ereignissen_
  - `DER.4.A14` [Hoch] Regelmäßige Überprüfung und Verbesserung der Notfallmaßnahmen — _DER.4 Notfallmanagement_
  - `INF.1.A36` [Standard] Regelmäßige Aktualisierungen der Dokumentation — _INF.1 Allgemeines Gebäude_
  - `OPS.1.1.1.A2` [Basis] Festlegung von Rollen und Berechtigungen für den IT-Betrieb — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `ORP.5.A8` [Standard] Regelmäßige Überprüfungen des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `APP.4.3.A20` [Standard] Regelmäßige Audits — _APP.4.3 Relationale Datenbanken_
  - `OPS.1.2.2.A13` [Standard] Regelmäßige Revision der Archivierungsprozesse — _OPS.1.2.2 Archivierung_
- **Begründung:** Gemittelte Kandidatenscores: DER.1.A1=0.44, DER.1.A13=0.44, DER.4.A14=0.44, INF.1.A36=0.44, OPS.1.1.1.A2=0.44, ORP.5.A8=0.44, APP.4.3.A20=0.33, OPS.1.2.2.A13=0.33
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8800 gs_ids=DER.4.A14;ORP.5.A8;OPS.1.1.1.A2;DER.1.A13;DER.1.A1;INF.1.A36
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6600 gs_ids=APP.4.3.A20;OPS.1.2.2.A13
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung BER.1.2 fordert eine regelmäßige und anlassbezogene Überprüfung von Verfahren und Regelungen auf Aktualität. Inhaltlich passen dazu vor allem DER.4.A14, ORP.5.A8, OPS.1.1.1.A2, DER.1.A13, DER.1.A1 und INF.1.A36, da diese jeweils die regelmäßige Prüfung, Aktualisierung bzw. Wirksamkeitskontrolle von Maßnahmen, Prozessen oder Dokumentationen verlangen. DER.4.A14 trifft den generischen Kern der regelmäßigen und anlassbezogenen Überprüfung von Maßnahmen und deren Verbesserung besonders gut. ORP.5.A8 deckt die regelmäßige Überprüfung von Management-Prozessen auf Effizienz und Effektivität ab. OPS.1.1.1.A2 behandelt die regelmäßige Prüfung und Anpassung von Rollen und Berechtigungen. DER.1.A13 und DER.1.A1 enthalten ebenfalls regelmäßige Überprüfungen von Systemen bzw. Richtlinien auf Aktualität und Wirksamkeit. INF.1.A36 fordert die regelmäßige Aktualisierung von Dokumentation auf aktuelle Gegebenheiten. Dennoch bleibt die GS++-Anforderung breiter, weil sie allgemein auf Verfahren und Regelungen der Berechtigung zielt und ausdrücklich anlassbezogene Prüfungen sowie den Kontext der Berechtigung insgesamt adressiert; diese breite, domänenübergreifende Prozessanforderung wird von den Kandidaten nur teilweise abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine, domänenunabhängige Überprüfung aller Berechtigungsverfahren und Regelungen sowie die explizit geforderte anlassbezogene Prüfung bei Ereignissen, strategischen Änderungen oder neuen rechtlichen Anforderungen. Die Kandidaten adressieren überwiegend einzelne Teilbereiche (Management-, Betriebs-, Detektions- oder Dokumentationsprozesse), nicht aber die Berechtigung als Gesamtprozess.

### BER.2.5 — Deaktivierung bei Weggang
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `OPS.2.3.A7` [Basis] Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses — _OPS.2.3 Nutzung von Outsourcing_
  - `ORP.2.A2` [Basis] Geregelte Verfahrensweise beim Weggang von Mitarbeitenden — _ORP.2 Personal_
- **Begründung:** Gemittelte Kandidatenscores: OPS.2.3.A7=0.42, ORP.2.A2=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=OPS.2.3.A7;ORP.2.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.2.3.A7 und ORP.2.A2 behandeln beide Aspekte des Weggangs, nämlich die organisatorische Beendigung von Beziehungen bzw. den Austritt von Mitarbeitenden. ORP.2.A2 fordert ausdrücklich, dass beim Verlassen der Institution Ausweise und Zutrittsberechtigungen eingezogen und betroffene Stellen informiert werden; das ist inhaltlich nah an der Deaktivierung von Berechtigungen. OPS.2.3.A7 fordert bei Beendigung eines Outsourcing-Verhältnisses zu prüfen, ob Zugangs-, Zutritts- und Zugriffsrechte aufgehoben wurden. Beide Anforderungen adressieren jedoch nur die Aufhebung bzw. den Entzug von Rechten im Beendigungsfall, nicht die explizite Deaktivierung der zugeordneten Identität selbst.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die explizite Deaktivierung oder Löschung der Identität als solche sowie die klare Zuordnung zum Identitätsmanagement; ORP.2.A2 ist vor allem personalorganisatorisch, OPS.2.3.A7 outsourcingbezogen. Beide treffen nicht die volle technische/administrative Steuerung einer Benutzeridentität bei Weggang.

### BER.6.8 — Kriterien für die Qualität von Passwörtern
- **Confidence:** 0.41
- **Gemappte GS-Anforderungen:**
  - `CON.1.A10` [Standard] Erstellung eines Kryptokonzepts — _CON.1 Kryptokonzept_
  - `CON.1.A9` [Standard] Festlegung von Kriterien für die Auswahl von Hard- oder Software mit kryptografischen Funktionen — _CON.1 Kryptokonzept_
- **Begründung:** Gemittelte Kandidatenscores: CON.1.A10=0.41, CON.1.A9=0.41
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8300 gs_ids=CON.1.A10;CON.1.A9
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.1.A9 und CON.1.A10 sind die einzigen Kandidaten mit echter inhaltlicher Nähe, da sie Kriterien für die Auswahl bzw. Ausgestaltung kryptografischer Funktionen festlegen und dabei TR-02102 berücksichtigen. Die GS++-Anforderung BER.6.8 verlangt jedoch explizit Kriterien für die Qualität von Passwörtern anhand von Lebensdauer und Angriffsmöglichkeiten; das umfasst z. B. Passwortlänge, Entropie, Symbolvielfalt sowie die Berücksichtigung von maximalen Passwortversuchen und Mehr-Faktor-Authentifizierung. Diese konkreten Passwortqualitätskriterien werden durch CON.1.A9/CON.1.A10 nicht geregelt. Daher nur teilweise Abdeckung.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die eigentlichen Passwortqualitätskriterien (z. B. Mindestlänge, Entropie, Symbolvielfalt), die Differenzierung nach Lebensdauer und Angriffsmöglichkeiten sowie die Ableitung der Anforderungen für Passwörter anhand von Kontenzahl, Rate-Limits oder MFA. Die Kandidaten adressieren nur kryptografische Auswahl-/Konzeptvorgaben, nicht Passwortregeln.

### BER.7.16.3 — Erneuerung
- **Confidence:** 0.37
- **Gemappte GS-Anforderungen:**
  - `CON.1.A4` [Basis] Geeignetes Schlüsselmanagement — _CON.1 Kryptokonzept_
  - `DER.2.3.A4` [Basis] Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln — _DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle_
- **Begründung:** Gemittelte Kandidatenscores: CON.1.A4=0.37, DER.2.3.A4=0.37
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7400 gs_ids=CON.1.A4;DER.2.3.A4
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] CON.1.A4 deckt den allgemeinen Teil des Schlüsselmanagements ab, indem es festlegt, dass Integrität und Authentizität von Schlüsseln sichergestellt werden müssen und dass mit abgelaufenen Schlüsseln/Zertifikaten umzugehen ist. DER.2.3.A4 deckt den Fall kompromittierter TLS-Schlüssel bzw. kompromittierter interner CAs ab und verlangt die Neuerzeugung, Verteilung sowie Sperrung/Rückruf kompromittierter Schlüssel und Zertifikate. Beide Anforderungen berühren damit die Erneuerung bzw. den Umgang mit gefährdeten Schlüsseln. Die spezifische GS++-Forderung, den Schlüssel bei der Erneuerung einer Beglaubigung anhand definierter Vorgaben aktiv zu testen (z. B. Signatur-, Fingerprint- oder Sperrlistenprüfung), wird jedoch nicht ausdrücklich und in dieser Detaillierung behandelt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die konkrete Prüflogik bei der Erneuerung einer Beglaubigung (explizites Testen des Schlüssels gegen Erneuerungsvorgaben), einschließlich der genannten Verifikationsarten wie Signaturprüfung, Fingerprint-Abgleich oder Validierung gegen Sperrlisten. Auch die enge PKI-/Zertifikatserneuerung mit Vertrauenskette wird nur indirekt angesprochen.

### BER.7.16.6 — Revocationstatus
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `DER.2.3.A4` [Basis] Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln — _DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.3.A4=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9300 gs_ids=DER.2.3.A4
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] DER.2.3.A4 deckt die GS++-Anforderung inhaltlich direkt ab: Dort wird gefordert, kompromittierte Schlüssel und Zertifikate zuverlässig zu sperren und zurückzurufen, also den Revocationstatus bzw. den Widerruf von Schlüsseln/Zertifikaten zu behandeln. Die GS++-Anforderung verlangt, den Revocationstatus eines Schlüssels im Verzeichnis öffentlicher Schlüssel zu dokumentieren; das ist funktional genau die Abbildung des zurückgezogenen Status nach Kompromittierung oder Unbrauchbarkeit. Die Domäne (Schlüssel-/Zertifikatsmanagement) und die Regelungsart (organisatorisch/technisch) passen zusammen.

## Keine Abdeckung (1)

### BER.3.15 — Keine Gruppenkonten
- **Confidence:** 0.49
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9800 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung BER.3.15 fordert, Gruppenkonten bzw. gemeinsam genutzte Zugangskonten zu untersagen, um die eindeutige Zuordnung von Handlungen zu einzelnen Personen zu gewährleisten. Keiner der Kandidaten behandelt das Verbot oder die Unzulässigkeit von Gruppenkonten inhaltlich. Am nächsten kommen noch Vorgaben zu getrennten Konten oder zur Trennung administrativer Tätigkeiten, etwa OPS.1.1.2.A22 und SYS.2.4.A3, diese regeln jedoch andere Zwecke (Abgrenzung administrativer/normaler Nutzung bzw. individuelle Konten auf macOS) und kein generelles Verbot gemeinsam genutzter Konten.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt ist das explizite Untersagen von gemeinsam genutzten Zugangskonten/Gruppenkonten für die Nachvollziehbarkeit von Handlungen. Die vorhandenen Kandidaten adressieren allenfalls Kontentrennung in anderen Kontexten oder individuelle Benutzerkonten auf einem System, nicht aber das generelle Verbot von Gruppenkonten.
