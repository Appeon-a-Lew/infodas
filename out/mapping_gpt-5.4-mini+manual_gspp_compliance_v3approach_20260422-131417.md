# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T13:14:17

**Gesamt:** 3 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 3 |
| Keine Abdeckung | 0 |

## Teilweise abgedeckt (3)

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
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=APP.6.A10;CON.8.A12;DER.4.A12;SYS.1.1.A11;SYS.4.4.A6;ORP.2.A1;IND.2.7.A1;NET.1.2.A12;DER.3.1.A6;APP.7.A6;CON.10.A11;IND.1.A11;APP.2.1.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.1.1.1 verlangt die Dokumentation von Verfahren und Regelungen auf architektonischer Ebene, also eine allgemeine, übergreifende Regelungsdokumentation. Das wird inhaltlich nur teilweise von mehreren Kandidaten getroffen: APP.6.A10, SYS.1.1.A11 und SYS.4.4.A6 verlangen die Dokumentation bzw. Zusammenfassung von Regelungen in einer Sicherheitsrichtlinie; APP.2.1.A1 fordert eine Sicherheitsrichtlinie für Verzeichnisdienste; IND.1.A11 verlangt dokumentierte Regelungen zu Informationssicherheit bei Beschaffung/Entwicklung; ORP.2.A1 adressiert das Informieren neuer Mitarbeitender über Regelungen, Handlungsanweisungen und Verfahrensweisen. Zusätzlich enthalten CON.8.A12, CON.10.A11, APP.7.A6, NET.1.2.A12, IND.2.7.A1 und DER.4.A12 Dokumentationspflichten für spezifische technische oder Prozessbereiche, und DER.3.1.A6 verlangt die Dokumentation eines Bewertungsschemas für Audits. Diese Kandidaten zeigen zwar das generelle Prinzip der Dokumentation, aber jeweils nur in engerem Fachkontext und nicht als vollständige, architekturweite Dokumentation aller Verfahren und Regelungen.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die übergreifende architekturspezifische Verbindlichkeit, die institutionenweite Zusammenführung aller Verfahren und Regelungen, die Zielgruppenorientierung der Dokumentationsstruktur sowie die explizite Ausrichtung auf Management und Umsetzung über verschiedene Rollen hinweg. Die Kandidaten sind überwiegend bereichsspezifisch (Software, Netz, OT, Server, Notfallmanagement, Audit) und ersetzen keine allgemeine Architektur-Dokumentation.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.82
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
- **Begründung:** Gemittelte Kandidatenscores: NET.1.1.A11=0.82, CON.7.A7=0.46, CON.7.A8=0.46, NET.1.1.A10=0.46, NET.1.1.A18=0.46, NET.1.1.A4=0.46, NET.2.1.A15=0.46, SYS.3.1.A8=0.46, SYS.3.2.1.A28=0.46, NET.3.3.A11=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9200 gs_ids=NET.1.1.A11;NET.1.1.A4;NET.1.1.A18;NET.1.1.A10;CON.7.A7;CON.7.A8;SYS.3.2.1.A28;NET.2.1.A15;SYS.3.1.A8
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] Die Anforderungen NET.1.1.A11, NET.1.1.A4, NET.1.1.A18 und NET.1.1.A10 decken den Kern der GS++-Anforderung ab, nämlich externe Internetanbindungen bzw. externe Netzanbindungen über Zonen, DMZ, Firewall und sichere Kommunikationskanäle zu begrenzen. CON.7.A7, CON.7.A8, SYS.3.2.1.A28, NET.2.1.A15 und SYS.3.1.A8 adressieren ergänzend mobile Systeme und deren abgesicherten bzw. eingeschränkten Internet- und VPN-Zugriff, was dem Hinweis auf mobile Systeme mit VPN oder Direct-Internet-Access entspricht. Zusammen zeigen diese Anforderungen eine technische Einschränkung und Absicherung externer Verbindungen, also die wesentliche Stoßrichtung von ARCH.2.2.1.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der allgemeine architektonische Sollsatz, externe Netzanschlüsse grundsätzlich einzuschränken und dabei explizit auch unerwünschte Ein- und Ausleitungen sowie Datenabflüsse zu minimieren. Die Kandidaten behandeln vor allem sichere Internetanbindung, VPN, DMZ und Firewall-Struktur; eine explizite, generische Architekturregel zur Begrenzung externer Netzanschlüsse für alle Segmente bzw. die direkte Vorgabe eines Direct-Internet-Access-Agenten fehlt. Außerdem ist die Regelung für mobile Systeme nur indirekt und nicht vollständig gleichwertig zur GS++-Formulierung.

### ARCH.5.1.8 — Inspektion verschlüsselter Verbindungen
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A21` [Standard] Temporäre Entschlüsselung des Datenverkehrs — _NET.3.2 Firewall_
  - `NET.3.2.A28` [Hoch] Zentrale Filterung von aktiven Inhalten — _NET.3.2 Firewall_
  - `NET.1.1.A12` [Basis] Absicherung ausgehender interner Kommunikation zum Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A20` [Standard] Absicherung von grundlegenden Internetprotokollen — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A21=0.46, NET.3.2.A28=0.46, NET.1.1.A12=0.34, NET.3.2.A20=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9100 gs_ids=NET.3.2.A28;NET.3.2.A21
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6855 gs_ids=NET.3.2.A20;NET.1.1.A12
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A28 adressiert die zentrale Filterung aktiver Inhalte und nennt ausdrücklich die Entschlüsselung verschlüsselten Datenverkehrs über Sicherheitsproxies, um Inhalte zu filtern. NET.3.2.A21 behandelt die temporäre Entschlüsselung verschlüsselter Verbindungen in nicht vertrauenswürdige Netze zur Protokollverifikation und Schadsoftwareprüfung. Beide Anforderungen decken damit den Kern der Inspektion verschlüsselter Verbindungen ab. Allerdings beschreibt die GS++-Anforderung breiter die Architektur für externe Netzanschlüsse und die Einschränkung/Inspektion von Verbindungen nach Inhalt, einschließlich allgemeiner Verbindungsinspektion und exemplarischer Endstelleninspektion; diese breitere Architektur- und Regelungslogik wird von den beiden Kandidaten nur teilweise erfasst.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die generelle architektonische Vorgabe für externe Netzanschlüsse sowie die inhaltliche Einschränkung aller unverschlüsselten und verschlüsselten Verbindungen nach Art des Inhalts. Die Kandidaten fokussieren auf zentrale Entschlüsselung/Proxy-Inspektion, nicht auf die vollständige Architekturregelung oder alternative Endstellen-Inspektion als allgemeines Konzept.
