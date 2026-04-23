# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:41:16

**Gesamt:** 5 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 5 |
| Keine Abdeckung | 0 |

## Teilweise abgedeckt (5)

### ARCH.1.1.1 — Dokumentation
- **Confidence:** 0.41
- **Gemappte GS-Anforderungen:**
  - `APP.6.A10` [Standard] Erstellung einer Sicherheitsrichtlinie für den Einsatz der Software — _APP.6 Allgemeine Software_
  - `APP.7.A6` [Standard] Dokumentation der Anforderungen an die Individualsoftware — _APP.7 Entwicklung von Individualsoftware_
  - `CON.8.A12` [Standard] Ausführliche Dokumentation — _CON.8 Software-Entwicklung_
  - `DER.3.1.A6` [Standard] Definition der Prüfungsgrundlage und eines einheitlichen Bewertungsschemas — _DER.3.1 Audits und Revisionen_
  - `IND.1.A11` [Standard] Sichere Beschaffung und Systementwicklung — _IND.1 Prozessleit- und Automatisierungstechnik_
  - `IND.2.7.A1` [Basis] Erfassung und Dokumentation — _IND.2.7 Safety Instrumented Systems_
  - `NET.1.2.A12` [Standard] Ist-Aufnahme und Dokumentation des Netzmanagements — _NET.1.2 Netzmanagement_
  - `SYS.1.1.A11` [Standard] Festlegung einer Sicherheitsrichtlinie für Server — _SYS.1.1 Allgemeiner Server_
  - `SYS.4.4.A6` [Standard] Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.6.A10=0.41, APP.7.A6=0.41, CON.8.A12=0.41, DER.3.1.A6=0.41, IND.1.A11=0.41, IND.2.7.A1=0.41, NET.1.2.A12=0.41, SYS.1.1.A11=0.41, SYS.4.4.A6=0.41
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8200 gs_ids=APP.6.A10;CON.8.A12;DER.3.1.A6;IND.1.A11;NET.1.2.A12;APP.7.A6;SYS.1.1.A11;SYS.4.4.A6;IND.2.7.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Mehrere Kandidaten adressieren den Aspekt der Dokumentation von Regeln, Verfahren oder Anforderungen, aber keiner deckt die GS++-Anforderung ARCH.1.1.1 vollständig und domänengleich ab. APP.6.A10, SYS.1.1.A11 und SYS.4.4.A6 verlangen jeweils, Regelungen für den Einsatz/Betrieb in einer Sicherheitsrichtlinie zusammenzufassen bzw. dokumentiert zu halten. CON.8.A12 und APP.7.A6 behandeln die Dokumentation im Entwicklungs-/Anwendungskontext, NET.1.2.A12 die Dokumentation eines Management-Aufbaus, IND.1.A11 die Dokumentation von Regelungen und deren Umsetzung bei OT-Beschaffung/Entwicklung, IND.2.7.A1 die Dokumentation von Komponenten und Zuständigkeiten, und DER.3.1.A6 die Dokumentation eines einheitlichen Bewertungsschemas für Audits. Diese Anforderungen überschneiden sich mit dem Dokumentationsgedanken, aber sie beziehen sich auf spezifische Fachdomänen oder auf Teilaspekte wie Richtlinien, Architektur, Auditgrundlagen oder Systeminventare. ARCH.1.1.1 verlangt allgemein, dass Architektur die Verfahren und Regelungen dokumentiert; die allgemeine, domänenübergreifende Pflicht zur Dokumentation von Verfahren und Regelungen wird durch die Kandidaten nur teilweise getroffen.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt ist die allgemeine, architekturbezogene Dokumentation von Verfahren und Regelungen als übergreifende Grundsatzanforderung. Die Kandidaten sind überwiegend domänenspezifisch (Webanwendung, Server, IoT, OT, Netzmanagement, Audit, SIS) oder behandeln nur Teilaspekte wie Sicherheitsrichtlinien, Dokumentation von Komponenten oder Audit-Bewertungsschemata. Es fehlt insbesondere die explizite Anforderung, architektonische Verfahren/Regelungen institutionenweit und unabhängig von einer konkreten technischen Domäne verbindlich zu dokumentieren.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.77
- **Gemappte GS-Anforderungen:**
  - `NET.3.3.A11` [Standard] Sichere Anbindung eines externen Netzes — _NET.3.3 VPN_
  - `CON.7.A7` [Basis] Sicherer Remote-Zugriff auf das Netz der Institution — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `CON.7.A8` [Basis] Sichere Nutzung von öffentlichen WLANs — _CON.7 Informationssicherheit auf Auslandsreisen_
  - `INF.10.A6` [Standard] Einrichtung sicherer Netzzugänge — _INF.10 Besprechungs-, Veranstaltungs- und Schulungsräume_
  - `NET.1.1.A10` [Basis] DMZ-Segmentierung für Zugriffe aus dem Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A18` [Standard] P-A-P-Struktur für die Internet-Anbindung — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `SYS.3.1.A8` [Standard] Sicherer Anschluss von Laptops an Datennetze — _SYS.3.1 Laptops_
  - `SYS.3.1.A9` [Basis] Sicherer Fernzugriff mit Laptops — _SYS.3.1 Laptops_
  - `SYS.3.2.1.A28` [Standard] Verwendung der Filteroption für Webseiten — _SYS.3.2.1 Allgemeine Smartphones und Tablets_
  - `NET.1.1.A11` [Basis] Absicherung eingehender Kommunikation vom Internet in das interne Netz — _NET.1.1 Netzarchitektur und -design_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.3.A11=0.77, CON.7.A7=0.41, CON.7.A8=0.41, INF.10.A6=0.41, NET.1.1.A10=0.41, NET.1.1.A18=0.41, NET.1.1.A4=0.41, SYS.3.1.A8=0.41, SYS.3.1.A9=0.41, SYS.3.2.1.A28=0.41, NET.1.1.A11=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8200 gs_ids=NET.1.1.A4;NET.1.1.A10;NET.1.1.A18;NET.3.3.A11;SYS.3.1.A9;CON.7.A7;CON.7.A8;INF.10.A6;SYS.3.1.A8;SYS.3.2.1.A28
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.2.2.1 fordert allgemein, Verbindungen über externe Netzanschlüsse in der Architektur einzuschränken, um Angriffsfläche, unerwünschte Ein-/Ausleitungen und Datenabfluss zu reduzieren. Inhaltlich passen dafür vor allem NET.1.1.A4, NET.1.1.A10, NET.1.1.A18 und NET.1.1.A9/NET.3.3.A11 sowie die mobilitätsbezogenen Anforderungen CON.7.A7, CON.7.A8, SYS.3.1.A9 und SYS.3.1.A8: NET.1.1.A4, NET.1.1.A10 und NET.1.1.A18 adressieren die Segmentierung und Absicherung externer Internet-Anbindungen über Firewall/DMZ/P-A-P-Struktur; NET.3.3.A11 beschränkt VPN-Verbindungen auf vorgesehene Systeme; CON.7.A7, CON.7.A8 und SYS.3.1.A9 verlangen für mobile bzw. öffentliche Netze sichere Kommunikationskanäle, insbesondere VPN, statt direkter Internet-/Netzzugriffe; SYS.3.1.A8 regelt den sicheren Anschluss von Laptops an eigene/fremde Netze. INF.10.A6 trifft eine ähnliche Aussage für externe Endgeräte in Besprechungs-/Schulungsräumen, und SYS.3.2.1.A28 erwähnt die VPN-Einbindung mobiler Endgeräte in Proxy-/Reputations-Infrastrukturen. Insgesamt wird damit die Einschränkung externer Verbindungen auf verschiedenen konkreten Ebenen teilweise abgedeckt. Vollständig ist es aber nicht, weil ARCH.2.2.1 als Architekturprinzip generell externe Netzanschlüsse einschränken soll, einschließlich der expliziten organisatorisch-architektonischen Vorgabe, welche externen Anschlüsse überhaupt vorgesehen sind und wie diese strategisch minimiert werden; diese generelle Architekturlenkung wird durch die Kandidaten nur indirekt über konkrete technische Schutzmaßnahmen adressiert.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die allgemeine architektonische Vorgabe zur Minimierung bzw. gezielten Beschränkung externer Netzanschlüsse als Designprinzip sowie die explizite Betrachtung aller externen Anschlussarten. Die Kandidaten behandeln vor allem konkrete technische Schutzmaßnahmen (VPN, Firewall, DMZ, P-A-P, mobile Zugriffe), aber keine umfassende Architekturentscheidung zur grundsätzlichen Reduktion externer Schnittstellen.

### ARCH.2.2.11 — Physische Segmentierung
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.1.1.A4` [Basis] Netztrennung in Zonen — _NET.1.1 Netzarchitektur und -design_
  - `OPS.1.1.2.A16` [Standard] Erweiterte Sicherheitsmaßnahmen für Administrationszugänge — _OPS.1.1.2 Ordnungsgemäße IT-Administration_
  - `SYS.1.5.A4` [Basis] Sichere Konfiguration eines Netzes für virtuelle Infrastrukturen — _SYS.1.5 Virtualisierung_
  - `SYS.1.5.A9` [Standard] Netzplanung für virtuelle Infrastrukturen — _SYS.1.5 Virtualisierung_
  - `SYS.1.8.A15` [Standard] Sichere Trennung von Mandanten in Speicherlösungen — _SYS.1.8 Speicherlösungen_
  - `SYS.2.5.A2` [Basis] Planung der verwendeten Netze für virtuelle Clients — _SYS.2.5 Client-Virtualisierung_
  - `SYS.2.6.A4` [Standard] Netzsegmentierung der VDI-Komponenten — _SYS.2.6 Virtual Desktop Infrastructure_
  - `NET.1.1.A22` [Standard] Spezifikation des Segmentierungskonzepts — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A23` [Standard] Trennung von Netzsegmenten — _NET.1.1 Netzarchitektur und -design_
  - `NET.1.1.A31` _(nicht im Korpus gefunden)_
  - `NET.1.1.A33` _(nicht im Korpus gefunden)_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.42, NET.1.1.A4=0.42, OPS.1.1.2.A16=0.42, SYS.1.5.A4=0.42, SYS.1.5.A9=0.42, SYS.1.8.A15=0.42, SYS.2.5.A2=0.42, SYS.2.6.A4=0.42, NET.1.1.A22=0.34, NET.1.1.A23=0.34, NET.1.1.A31=0.34, NET.1.1.A33=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=SYS.1.5.A9;NET.1.1.A4;SYS.1.5.A4;INF.14.A6;SYS.1.8.A15;SYS.2.5.A2;SYS.2.6.A4;OPS.1.1.2.A16
[manual:gspp_compliance_v3approach] coverage=teilweise confidence=0.6711 gs_ids=NET.1.1.A31;NET.1.1.A23;NET.1.1.A33;NET.1.1.A22
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung ARCH.2.2.11 fordert physische Segmentierung bzw. eine physische Trennung von Netzen, um Umgehungen der Netztrennung möglichst zu vermeiden. Inhaltlich am nächsten liegen NET.1.1.A4, INF.14.A6, SYS.1.5.A4, SYS.1.5.A9, SYS.1.8.A15, SYS.2.5.A2, SYS.2.6.A4 und OPS.1.1.2.A16, weil sie jeweils Netztrennung, Segmentierung oder die Verhinderung der Umgehung bestehender Sicherheitsmechanismen behandeln. NET.1.1.A4 und INF.14.A6 verlangen explizite Trennung von Netzen bzw. Zonen und Absicherung der Übergänge, SYS.1.5.A4 und SYS.1.5.A9 adressieren die sichere Trennung in virtuellen Infrastrukturen, SYS.1.8.A15 behandelt Segmentierung zur Trennung von Mandanten in Speicherlösungen, SYS.2.5.A2 und SYS.2.6.A4 fordern Netztrennung für virtuelle Clients bzw. VDI-Komponenten, und OPS.1.1.2.A16 trennt Admin-Netze von produktiven Netzen. Allerdings ist die GS++-Anforderung spezifisch auf physische Segmentierung als bevorzugte Schutzmaßnahme ausgerichtet; mehrere Kandidaten erlauben nur logische bzw. virtualisierte Trennung oder behandeln nur spezielle Anwendungsfälle. Daher ist nur eine teilweise Abdeckung gegeben.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der Kernaspekt der expliziten physischen Segmentierung als generelles Architekturprinzip für Netze. Viele Kandidaten verlangen lediglich logische Trennung, Firewall-Abschirmung oder virtuelle Segmentierung und nicht zwingend eine physische Trennung. Außerdem decken die Kandidaten überwiegend Spezialfälle (Virtualisierung, VDI, GA, Storage, Admin-Netze) ab, aber keine allgemeine, bausteinübergreifende Anforderung, Netze physisch zu separieren, wenn dies architektonisch möglich bzw. gewünscht ist.

### ARCH.5.1.12 — Software-definierte Verbindungen
- **Confidence:** 0.41
- **Gemappte GS-Anforderungen:**
  - `INF.14.A6` [Basis] Separierung von Netzen der GA — _INF.14 Gebäudeautomation_
  - `NET.3.2.A2` [Basis] Festlegen der Firewall-Regeln — _NET.3.2 Firewall_
  - `NET.3.4.A6` [Standard] Festlegung von Notfallprozessen für NAC — _NET.3.4 Network Access Control_
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.41, NET.3.2.A2=0.41, NET.3.4.A6=0.41
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8100 gs_ids=NET.3.2.A2;INF.14.A6;NET.3.4.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A2 passt insofern, als dort verbindliche Firewall-Regeln und der Allowlist-Ansatz zur Beschränkung von Kommunikationsverbindungen gefordert werden. INF.14.A6 deckt die logische Trennung von Netzen sowie die kontrollierte und reglementierte Kommunikation an Segmentgrenzen ab und verlangt dafür mindestens Firewall-Funktion. NET.3.4.A6 ist nur insoweit anschlussfähig, als NAC-Mechanismen dynamisch auf Zustände reagieren können, beschreibt aber primär Notfallprozesse und keine dynamische Verbindungssteuerung. Zusammen treffen die Kandidaten den allgemeinen Gedanken der Verbindungsbeschränkung, aber nicht den Kern von software-definierten Verbindungen mit dynamischen, kontextabhängigen Kriterien/Policy-Engines.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die wesentlichen GS++-Aspekte dynamischer Kriterien bzw. kontextabhängiger Bewertung (z. B. Device Posture, Standort, Auslastung, Risikobewertung), die explizit software-definierte bzw. adaptive Verbindungsentscheidungen ermöglichen. Die Kandidaten beschreiben überwiegend statische Firewall-/Segmentierungsregeln oder organisatorische Notfallprozesse; echte dynamische, zustandsbasierte Policy-Entscheidungen werden nicht inhaltlich gefordert.

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
[gpt-5.4-mini] NET.3.2.A21 passt inhaltlich am besten, da dort ausdrücklich die temporäre Entschlüsselung verschlüsselter Verbindungen in nicht vertrauenswürdige Netze zur Protokollverifikation und Schadsoftwareprüfung gefordert wird. Das deckt den Kern der GS++-Anforderung zur Inspektion verschlüsselter Verbindungen ab. Allerdings beschreibt die GS++-Anforderung allgemeiner die Einschränkung und Inspektion des Inhalts verschlüsselter Verbindungen je nach Inhaltsart, inklusive expliziter Proxy-/Endstellen-Inspektion und allgemeiner Architekturvorgaben für externe Netzanschlüsse. Diese weitergehenden Architektur- und Inhaltsfilter-Aspekte werden von NET.3.2.A21 nur teilweise abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die allgemeine Architekturrichtlinie zur Einschränkung von Inhalten verschlüsselter Verbindungen je nach Inhaltsart sowie die breitere Inspektionsstrategie über Sicherheitsproxies oder Endstelleninspektion unabhängig vom konkreten Firewall-/TLS-Proxy-Kontext. Auch die allgemeine Proxy-Funktion als Vermittler zum Filtern/Blockieren wird nur implizit, nicht als Architekturvorgabe, behandelt.
