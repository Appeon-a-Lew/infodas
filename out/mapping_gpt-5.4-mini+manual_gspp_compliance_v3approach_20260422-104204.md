# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:42:04

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
  - `IND.2.7.A1` [Basis] Erfassung und Dokumentation — _IND.2.7 Safety Instrumented Systems_
  - `NET.1.2.A12` [Standard] Ist-Aufnahme und Dokumentation des Netzmanagements — _NET.1.2 Netzmanagement_
  - `SYS.1.1.A11` [Standard] Festlegung einer Sicherheitsrichtlinie für Server — _SYS.1.1 Allgemeiner Server_
  - `SYS.4.4.A6` [Standard] Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution — _SYS.4.4 Allgemeines IoT-Gerät_
- **Begründung:** Gemittelte Kandidatenscores: APP.6.A10=0.41, APP.7.A6=0.41, CON.8.A12=0.41, IND.2.7.A1=0.41, NET.1.2.A12=0.41, SYS.1.1.A11=0.41, SYS.4.4.A6=0.41
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8300 gs_ids=APP.6.A10;CON.8.A12;NET.1.2.A12;IND.2.7.A1;SYS.1.1.A11;SYS.4.4.A6;APP.7.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die GS++-Anforderung ARCH.1.1.1 fordert allgemein die Dokumentation von Verfahren und Regelungen. Dies wird inhaltlich nur teilweise durch mehrere Kandidaten aufgegriffen: APP.6.A10 verlangt die Zusammenfassung von Regelungen zum Einsatz und Betrieb von Software in einer Sicherheitsrichtlinie und deren Bekanntheit; CON.8.A12 fordert ausführliche Projekt-, Funktions-, Schnittstellen- und Betriebsdokumentation; NET.1.2.A12 verlangt eine vollständige und aktuelle Dokumentation des Netzmanagements; IND.2.7.A1 fordert die gesonderte Erfassung und Dokumentation aller zu einem SIS gehörenden Komponenten, Informationen, Verbindungen sowie Rollen und Zuständigkeiten; SYS.1.1.A11 und SYS.4.4.A6 verlangen jeweils Sicherheitsrichtlinien für Server bzw. IoT-Geräte sowie deren dokumentierte Umsetzung; APP.7.A6 fordert die umfassende Dokumentation von Anforderungen und Sicherheitsanforderungen an Individualsoftware. Diese Anforderungen treffen den Dokumentationsaspekt und teilweise auch die Verbindlichkeit von Regeln, aber sie sind jeweils auf bestimmte Domänen (Software, Netz, Server, IoT, SIS) bezogen und decken nicht allgemein die Dokumentation aller architektonischen Verfahren und Regelungen der Institution ab.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt ist die allgemeine, domänenübergreifende Dokumentation aller Architektur-Verfahren und Regelungen auf Institutionsebene. Insbesondere fehlt die explizite Anforderung, die Dokumentation zielgruppenorientiert als verbindliche Grundlage für Management und Umsetzung aller Architekturregeln zu strukturieren. Die Kandidaten sind überwiegend fach-/systembezogen statt allgemeingültig-organisatorisch.

### ARCH.2.2.1 — Externe Netzanschlüsse
- **Confidence:** 0.75
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
- **Begründung:** Gemittelte Kandidatenscores: NET.3.3.A11=0.75, CON.7.A7=0.39, CON.7.A8=0.39, INF.10.A6=0.39, NET.1.1.A10=0.39, NET.1.1.A18=0.39, NET.1.1.A4=0.39, SYS.3.1.A8=0.39, SYS.3.1.A9=0.39, SYS.3.2.1.A28=0.39, NET.1.1.A11=0.36
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7800 gs_ids=NET.1.1.A10;NET.1.1.A4;NET.1.1.A18;CON.7.A7;CON.7.A8;SYS.3.1.A9;NET.3.3.A11;SYS.3.1.A8;INF.10.A6;SYS.3.2.1.A28
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.7116 gs_ids=NET.3.3.A11;NET.1.1.A11
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung ARCH.2.2.1 verlangt, Verbindungen über externe Netzanschlüsse architektonisch einzuschränken, um die Angriffsfläche zu reduzieren und unerwünschte Ein- und Ausleitungen zu begrenzen. Das wird inhaltlich teilweise durch NET.1.1.A10 und NET.1.1.A4 abgedeckt, da beide die Internet-/Außenanbindung über externe DMZ, Firewalls und Netztrennung absichern. NET.1.1.A18 ergänzt dies durch die P-A-P-Struktur und damit die kontrollierte Entkopplung von Internetverkehr. Für mobile Systeme und externe Zugänge greifen CON.7.A7, CON.7.A8, SYS.3.1.A9, NET.3.3.A11 und SYS.3.1.A8, weil sie sicheren Remote-Zugriff, VPN-Nutzung und den sicheren Anschluss an externe Netze regeln. INF.10.A6 deckt den Ausschluss von gleichzeitigen internen und externen Verbindungen in Besprechungs-/Schulungsräumen ab. SYS.3.2.1.A28 behandelt die VPN-gestützte Einbindung mobiler Endgeräte in eine Proxy-/Reputations-Infrastruktur. Insgesamt adressieren die Kandidaten wichtige Teilaspekte der Einschränkung externer Verbindungen, aber nicht die allgemeine architektonische Forderung, externe Netzanschlüsse grundsätzlich und breit über alle Netzsegmente hinweg zu begrenzen.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist die allgemeine, netzarchitektonische Vorgabe, externe Netzanschlüsse als Designprinzip systemweit zu begrenzen. Die Kandidaten fokussieren vor allem Internetanbindung, VPN/Remote-Zugriff, mobile Systeme und einzelne Sonderfälle (VoIP, Besprechungsräume), aber nicht ausdrücklich eine umfassende Architekturregel für alle externen Netzanschlüsse und alle Segmentverbindungen. Zudem wird der Aspekt der direkten Absicherung von externen Netzanschlüssen für alle Netzarten nicht vollständig und generisch beschrieben.

### ARCH.2.2.11 — Physische Segmentierung
- **Confidence:** 0.42
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
- **Begründung:** Gemittelte Kandidatenscores: INF.14.A6=0.42, NET.1.1.A4=0.42, NET.4.2.A4=0.42, OPS.1.1.2.A16=0.42, SYS.1.5.A4=0.42, SYS.1.8.A15=0.42, NET.1.1.A22=0.34, NET.1.1.A23=0.34, NET.1.1.A31=0.34, NET.1.1.A33=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=NET.1.1.A4;SYS.1.5.A4;INF.14.A6;OPS.1.1.2.A16;SYS.1.8.A15;NET.4.2.A4
[manual:gspp_compliance_v3approach] coverage=teilweise confidence=0.6711 gs_ids=NET.1.1.A31;NET.1.1.A23;NET.1.1.A33;NET.1.1.A22
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung ARCH.2.2.11 zielt allgemein auf physische Segmentierung bzw. darauf, Netztrennung nicht nur virtuell, sondern möglichst auf physischer Ebene zu realisieren. NET.1.1.A4 passt insofern, als dort Netztrennung der Zonen ausdrücklich physisch separiert und über Firewalls abgesichert werden muss. SYS.1.5.A4 deckt den Aspekt ab, dass bestehende Sicherheitsmechanismen nicht über virtuelle Netze umgangen werden dürfen, was die Bevorzugung physischer statt rein virtueller Trennung stützt. INF.14.A6 enthält ebenfalls die Forderung nach Separierung von Netzen und kontrollierten Übergängen, einschließlich netzseitiger Separation in bestimmten Fällen. OPS.1.1.2.A16 behandelt die physische Trennung von Administrations- und produktiven Netzen, also eine physische Segmentierung für einen konkreten Zweck. SYS.1.8.A15 und NET.4.2.A4 enthalten ebenfalls Teilaspekte der Trennung von Netzen bzw. der Verhinderung direkter Verbindungen aus unsicheren Netzen. Insgesamt wird die Stoßrichtung der physischen bzw. netzseitigen Segmentierung getroffen, aber die GS++-Anforderung fordert als allgemeines Architekturprinzip die physische Zugangsbeschränkung von Netzen; diese generelle, architekturelle Aussage wird durch die Kandidaten nur teilweise abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der allgemeine architekturelle Grundsatz, Netze bevorzugt physisch statt nur logisch/virtuell zu trennen. Einige Kandidaten adressieren nur Spezialfälle (Virtualisierung, Verwaltung, GA, VoIP, Speicherlösungen) oder setzen Trennung mit Firewall-/Segmentierungsmaßnahmen gleich, ohne die physische Segmentierung als generelles Architekturprinzip umfassend zu verlangen.

### ARCH.5.1.12 — Software-definierte Verbindungen
- **Confidence:** 0.26
- **Gemappte GS-Anforderungen:**
  - `NET.3.4.A6` [Standard] Festlegung von Notfallprozessen für NAC — _NET.3.4 Network Access Control_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.4.A6=0.26
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.5200 gs_ids=NET.3.4.A6
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] NET.3.4.A6 behandelt Network Access Control und damit die technische Steuerung von Verbindungen anhand von Sicherheitsmechanismen und Notfall-/RADIUS-down-Policies. Das berührt den Grundgedanken der dynamisch beeinflussbaren Zugriffsentscheidung auf Verbindungen. Die GS++-Anforderung ARCH.5.1.12 geht jedoch spezifischer auf software-definierte Verbindungen ein, also auf logisch kontrollierte Netzwerkpfade, deren Zulassung anhand aktueller kontextabhängiger Merkmale wie Gerätezustand, Auslastung, Standort oder Risikobewertung bewertet wird. Diese explizit dynamische, kontextbasierte Pfadsteuerung wird durch NET.3.4.A6 nicht vollständig beschrieben. Die übrigen Kandidaten betreffen statische ACLs/Firewall-Regeln, VPN-/Fernwartungs- oder allgemeine Separierungs-/Beschaffungsthemen und bilden den Kern von software-definierten, dynamischen Verbindungen nicht passend ab.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die explizite Nutzung dynamischer Kontextmerkmale (z. B. device posture, Standort, Risikobewertung), die Entscheidung über logisch kontrollierte Netzwerkpfade im Sinne von SDN/Mikrosegmentierung sowie die Anpassung der Verbindungsfreigabe an aktuelle Betriebszustände. NET.3.4.A6 deckt eher NAC-Notfallmechanismen als software-definierte Verbindungen ab.

### ARCH.5.1.8 — Inspektion verschlüsselter Verbindungen
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `NET.3.2.A21` [Standard] Temporäre Entschlüsselung des Datenverkehrs — _NET.3.2 Firewall_
  - `NET.1.1.A12` [Basis] Absicherung ausgehender interner Kommunikation zum Internet — _NET.1.1 Netzarchitektur und -design_
  - `NET.3.2.A20` [Standard] Absicherung von grundlegenden Internetprotokollen — _NET.3.2 Firewall_
- **Begründung:** Gemittelte Kandidatenscores: NET.3.2.A21=0.48, NET.1.1.A12=0.34, NET.3.2.A20=0.34
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9700 gs_ids=NET.3.2.A21
[manual:gspp_compliance_v3approach] coverage=voll confidence=0.6855 gs_ids=NET.3.2.A20;NET.1.1.A12
Model-Begründungen:
[gpt-5.4-mini] NET.3.2.A21 passt inhaltlich am besten, weil es genau die temporäre Entschlüsselung verschlüsselter Verbindungen in nicht vertrauenswürdige Netze zum Zweck der Protokollverifikation und Schadsoftware-Prüfung beschreibt, also die eigentliche Inspektion verschlüsselter Verbindungen. Die GS++-Anforderung ARCH.5.1.8 geht jedoch weiter: Sie beschreibt allgemein die Architektur für externe Netzanschlüsse und verlangt, den Inhalt unverschlüsselter und verschlüsselter Verbindungen basierend auf der Art des Inhalts einzuschränken. Dieser allgemeine Architektur-/Perimeteraspekt sowie die inhaltliche Steuerung von Verbindungen werden durch NET.3.2.A21 nicht vollständig abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die allgemeine Architekturvorgabe für externe Netzanschlüsse und die generelle Einschränkung des Inhalts unverschlüsselter und verschlüsselter Verbindungen nach Inhaltsart. Ebenfalls fehlt die breitere perimeterschutzbezogene Regelung; abgedeckt ist nur die technische TLS-Entschlüsselung/Inspektion in nicht vertrauenswürdigen Netzen.
