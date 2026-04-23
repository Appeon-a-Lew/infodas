# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T11:35:51

**Gesamt:** 8 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 6 |
| Keine Abdeckung | 2 |

## Teilweise abgedeckt (6)

### GC.2.1 — Festlegung des externen Kontextes der Institution
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A1=0.46, ORP.5.A4=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9100 gs_ids=ORP.5.A1;ORP.5.A4
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A1 deckt den Kern der Anforderung ab, weil dort alle gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement identifiziert und dokumentiert werden müssen. ORP.5.A4 ergänzt dies, indem ein Prozess zur Identifikation relevanter gesetzlicher, vertraglicher und sonstiger Vorgaben aufgebaut und der Überblick über rechtliche Anforderungen organisiert werden soll. Beide Anforderungen beziehen sich jedoch primär auf rechtliche, vertragliche und compliance-bezogene Rahmenbedingungen. Die GS++-Anforderung verlangt darüber hinaus ausdrücklich die Analyse und Priorisierung weiterer externer Kontextfaktoren wie gesellschaftliche/kulturelle, technologische, wirtschaftliche sowie ökologische/physische Umweltbedingungen, was durch die Kandidaten nicht vollständig abgedeckt wird.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind insbesondere die systematische Erfassung, Integration und Priorisierung nicht-rechtlicher externer Faktoren (gesellschaftliche und kulturelle Erwartungen, technologische Entwicklungen, wirtschaftliche Marktbedingungen sowie ökologische und physische Umweltbedingungen).

### GC.3.1 — Analyse der externen interessierten Parteien
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A2=0.46, ORP.5.A4=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9100 gs_ids=ORP.5.A4;ORP.5.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A4 und ORP.5.A2 treffen den Kern der Anforderung teilweise, weil beide das Ermitteln und Verarbeiten von sicherheitsrelevanten Vorgaben bzw. Anforderungen für das Informationssicherheitsmanagement adressieren. ORP.5.A4 fordert einen Prozess zur Identifikation aller relevanten gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement und deren Überführung in Compliance-Prozesse. ORP.5.A2 verlangt, dass sicherheitsrelevante Anforderungen bei Planung, Konzeption und Beschaffung einfließen und Verantwortlichkeiten für die Einhaltung festgelegt werden. Damit ist die allgemeine systematische Aufnahme von Anforderungen in das ISMS abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der spezifische Fokus auf externe interessierte Parteien als solche (z. B. Kunden, Öffentlichkeit, Aufsichtsbehörden, Dienstleister) sowie das explizite Verfahren zu deren Bedürfnissen und Erwartungen. Ebenfalls fehlt die ausdrückliche Bewertung von Relevanz und Priorität dieser Stakeholder-Anforderungen und die Entscheidung, welche davon als verbindliche Verpflichtungen ins ISMS aufgenommen werden.

### GC.5.1.1 — Festlegung der Geschäftsprozesse
- **Confidence:** 0.39
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.1.A12` [Standard] Spezifikation und Umsetzung klarer Betriebsprozesse — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `OPS.2.2.A1` [Basis] Erstellung einer Strategie für die Cloud-Nutzung — _OPS.2.2 Cloud-Nutzung_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A8` [Standard] Regelmäßige Überprüfungen des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.1.A12=0.39, OPS.2.2.A1=0.39, ORP.5.A4=0.39, ORP.5.A8=0.39
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7800 gs_ids=OPS.1.1.1.A12;ORP.5.A4;ORP.5.A8;OPS.2.2.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A4 passt inhaltlich am ehesten, weil dort geeignete Prozesse und Organisationsstrukturen aufgebaut werden sollen, um relevante Anforderungen und Zuständigkeiten im Compliance-Kontext zu beherrschen; das berührt die Festlegung relevanter Geschäftsprozesse jedoch nur indirekt. OPS.1.1.1.A12 deckt den Aspekt ab, für Aufgaben Betriebsprozesse zu spezifizieren und Schnittstellen festzulegen, was der formalen Prozessfestlegung ähnelt, aber auf den IT-Betrieb begrenzt ist. OPS.1.1.1.A12 ist daher nur eine Teillösung für die geforderte Festlegung der für den Geltungsbereich relevanten Geschäftsprozesse. ORP.5.A8 behandelt die regelmäßige Überprüfung von Compliance-Prozessen und deren Angemessenheit, nicht aber deren erstmalige Festlegung; es unterstützt die Governance-Perspektive nur am Rand. OPS.2.2.A1 verlangt zwar die Festlegung einer Cloud-Nutzungsstrategie mit Zielen, Rahmenbedingungen und der Festlegung zukünftig bezogener Dienste, bezieht sich aber nur auf Cloud-Nutzung und nicht allgemein auf relevante Geschäftsprozesse. Insgesamt wird die allgemeine Pflicht, die für den Geltungsbereich relevanten Geschäftsprozesse festzulegen, nur teilweise abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die allgemeine, bereichsübergreifende Festlegung aller für den Geltungsbereich relevanten Geschäftsprozesse sowie die explizite Herleitung aus bestehenden Prozesslandkarten oder Hilfsprozessen. Die Kandidaten sind entweder auf Compliance, IT-Betrieb oder Cloud-Nutzung begrenzt und ersetzen keine vollständige Prozesslandkarte für die Institution.

### GC.6.1.4 — Freigabe der Sicherheitsleitlinie
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** Gemittelte Kandidatenscores: ISMS.1.A3=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9700 gs_ids=ISMS.1.A3
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ISMS.1.A3 deckt die Anforderung direkt ab: Dort muss die Institutionsleitung eine übergeordnete Leitlinie zur Informationssicherheit verabschieden. Die GS++-Anforderung GC.6.1.4 verlangt ebenfalls, dass die festgelegte Sicherheitsleitlinie durch die Institutionsleitung autorisiert wird. Inhaltlich ist das dieselbe Freigabe-/Verabschiedungsfunktion durch die Leitung.

### GC.7.1 — Verfahren und Regelungen
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A1=0.47, ORP.5.A2=0.47, ORP.5.A4=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9300 gs_ids=ORP.5.A4;ORP.5.A1;ORP.5.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A1 deckt die Pflicht ab, alle für das Informationssicherheitsmanagement relevanten gesetzlichen, vertraglichen und sonstigen Vorgaben zu identifizieren und zu dokumentieren. ORP.5.A4 ergänzt dies um den Aufbau eines Prozesses zur Identifikation relevanter Vorgaben sowie geeigneter Prozesse und Organisationsstrukturen, um den Überblick über die rechtlichen Anforderungen zu gewährleisten und Sicherheitsanforderungen zu integrieren. ORP.5.A2 ergänzt die operative Beachtung der identifizierten Anforderungen in Planung, Konzeption und Beschaffung sowie die Festlegung von Verantwortlichkeiten und Maßnahmen zur Vermeidung von Verstößen. Zusammen bilden diese Anforderungen inhaltlich das geforderte Verfahren zur Sammlung, Integration und Priorisierung aller für das Informationssicherheitsmanagement relevanten Rahmenbedingungen ab.

### GC.8.1.1.1.1 — Vorspracherecht des Informationssicherheitsbeauftragten
- **Confidence:** 0.93
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A12` [Standard] Management-Berichte zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** ISMS.1.A1 deckt die grundsätzliche Verantwortung der Institutionsleitung ab, sich regelmäßig über den Status der Informationssicherheit informieren zu lassen. ISMS.1.A4 deckt ab, dass der oder die ISB die Möglichkeit haben muss, bei Bedarf direkt an die Institutionsleitung zu berichten. ISMS.1.A12 ergänzt die regelmäßige Management-Berichterstattung des ISB an die Institutionsleitung über den Stand der Informationssicherheit. Zusammen treffen diese Anforderungen den Berichts- und Informationsfluss zwischen ISB und Leitung, aber sie verankern nicht ausdrücklich ein direktes Vorspracherecht des ISB als verbindliches Recht ohne Zwischenschaltung anderer Stellen.
- **Lücken:** Nicht explizit abgedeckt ist die verbindliche Verankerung eines direkten Vorspracherechts des ISB bei der Institutionsleitung als eigenständiges Recht. Die Kandidaten regeln nur Informationspflichten, Berichtsmöglichkeiten und regelmäßige Berichte, aber nicht die formale Zusicherung, dass der ISB jederzeit direkt und ohne Vermittlung vorsprechen darf.

## Keine Abdeckung (2)

### GC.3.2 — Analyse der internen interessierten Parteien
- **Confidence:** 0.48
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9700 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidatenanforderungen adressiert das geforderte Verfahren zum Ermitteln aller internen interessierten Parteien sowie deren Bedürfnisse und Erwartungen an das Informationssicherheitsmanagement. ORP.5.A4 und ORP.5.A8 behandeln Compliance-Management bzw. dessen Überprüfung, nicht die Stakeholder-Analyse. Die übrigen Kandidaten betreffen Vorfälle, Administration, Forensik, Datenbanken, DNS, Apps, Netzmanagement oder Outsourcing und sind thematisch bzw. regelungsbezogen nicht einschlägig.
- **Lücken:** [gpt-5.4-mini] Abgedeckt wären nur allgemeine Compliance-/Betriebsaspekte, nicht jedoch die systematische Identifikation interner interessierter Parteien (z. B. Geschäftsführung, Mitarbeitende, Führungskräfte, Betriebsrat/Personalrat) und die Ermittlung ihrer Bedürfnisse und Erwartungen an das ISMS.

### GC.7.1.2 — Anhörung zuständiger Stellen
- **Confidence:** 0.48
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9700 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidaten beschreibt die Anhörung zuständiger Stellen zur Dokumentation von Compliance-Verpflichtungen. ORP.5.A4 und ORP.5.A8 betreffen Aufbau, Identifikation und Überprüfung des Compliance Managements, aber nicht die Einbindung/Anhörung fachlich zuständiger Stellen. DER.2.1.A4 und DER.2.2.A1 regeln die Einbeziehung von Datenschutzbeauftragten, Rechtsabteilung oder Betriebsrat in spezifischen Vorfällen bzw. Forensik, jedoch nicht allgemein die Anhörung zuständiger Stellen bei der Compliance-Dokumentation. Die übrigen Kandidaten sind thematisch noch weiter entfernt.
- **Lücken:** [gpt-5.4-mini] Es fehlt die explizite Anforderung, bei der Erfassung/Dokumentation von Compliance-Verpflichtungen die zuständigen internen Stellen systematisch anzuhören (z. B. Rechtsabteilung, Datenschutz, Brandschutz, Fachverantwortliche).
