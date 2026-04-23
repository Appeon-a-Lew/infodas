# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T11:10:20

**Gesamt:** 8 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 6 |
| Keine Abdeckung | 2 |

## Teilweise abgedeckt (6)

### GC.2.1 — Festlegung des externen Kontextes der Institution
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A1=0.48, ORP.5.A4=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9700 gs_ids=ORP.5.A1;ORP.5.A4
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A1 passt inhaltlich, weil die Anforderung die Identifikation und Dokumentation aller gesetzlichen, vertraglichen und sonstigen Vorgaben mit Einfluss auf das Informationssicherheitsmanagement verlangt. ORP.5.A4 ergänzt dies, indem ein Prozess zur Identifikation aller relevanten gesetzlichen, vertraglichen und sonstigen Vorgaben sowie deren Integration ins Compliance Management gefordert wird. Beide Anforderungen decken damit den rechtlichen/regulatorischen Teil der externen Rahmenbedingungen und den organisatorischen Umgang damit ab. Die GS++-Anforderung GC.2.1 geht jedoch deutlich weiter, weil sie zusätzlich gesellschaftliche und kulturelle Faktoren, technologische Entwicklungen, wirtschaftliche Bedingungen sowie ökologische und physische Umweltbedingungen systematisch erfassen, integrieren und priorisieren verlangt. Diese externen Kontextfaktoren werden von ORP.5.A1 und ORP.5.A4 nicht abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die systematische Betrachtung und Priorisierung nicht-rechtlicher externer Kontextfaktoren, insbesondere gesellschaftliche/kulturelle, technologische, wirtschaftliche sowie ökologische und physische Umweltbedingungen. Außerdem wird die explizite Priorisierung aller externen Rahmenbedingungen nicht vollständig getroffen.

### GC.3.1 — Analyse der externen interessierten Parteien
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A2=0.45, ORP.5.A4=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=ORP.5.A4;ORP.5.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A4 und ORP.5.A2 greifen den organisatorischen Kern der Anforderung auf, nämlich relevante Vorgaben bzw. Anforderungen zu identifizieren und bei Planung, Konzeption und im Compliance Management zu berücksichtigen. ORP.5.A4 fordert ausdrücklich, alle relevanten gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement zu identifizieren und zu strukturieren; ORP.5.A2 verlangt, sicherheitsrelevante Anforderungen in die Planung einzubeziehen und Verantwortlichkeiten festzulegen. Damit ist die Ermittlung und Behandlung externer Anforderungen teilweise abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die spezifischen Aspekte der GS++-Anforderung: das systematische Ermitteln aller externen interessierten Parteien als solche, die Bewertung ihrer Bedürfnisse und Erwartungen, die Priorisierung dieser Anforderungen sowie die explizite Entscheidung, welche Anforderungen als verbindliche Verpflichtungen ins ISMS aufgenommen werden. Die Kandidaten sprechen allgemeine Compliance-/Anforderungsidentifikation an, aber nicht die Stakeholder-Analyse im geforderten Umfang.

### GC.6.1.4 — Freigabe der Sicherheitsleitlinie
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** Gemittelte Kandidatenscores: ISMS.1.A3=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9700 gs_ids=ISMS.1.A3
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ISMS.1.A3 passt inhaltlich, weil dort die Institutionsleitung eine Leitlinie zur Informationssicherheit verabschieden soll. Die GS++-Anforderung GC.6.1.4 verlangt jedoch spezifisch die Autorisierung/Freigabe der festgelegten Sicherheitsleitlinie durch die Institutionsleitung, also den formalen Freigabeakt. ISMS.1.A3 deckt die inhaltliche Erstellung und Verabschiedung der Leitlinie durch die Leitung ab, aber die explizite Autorisierung als eigener Regelungsgehalt ist nicht in gleicher Klarheit enthalten.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt ist der explizite formale Freigabe-/Autorisierungsakt der bereits festgelegten Sicherheitsleitlinie. ISMS.1.A3 beschreibt vor allem Erstellung, Verabschiedung und Bekanntgabe der Leitlinie.

### GC.7.1 — Verfahren und Regelungen
- **Confidence:** 0.46
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A1=0.46, ORP.5.A2=0.46, ORP.5.A4=0.46
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9200 gs_ids=ORP.5.A4;ORP.5.A1;ORP.5.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A4, ORP.5.A1 und ORP.5.A2 decken die GS++-Anforderung inhaltlich gemeinsam ab: ORP.5.A1 fordert die Identifikation und Dokumentation aller gesetzlichen, vertraglichen und sonstigen Vorgaben mit Relevanz für das Informationssicherheitsmanagement; ORP.5.A4 verlangt dazu einen Prozess zur Identifikation relevanter Vorgaben sowie geeignete Prozesse und Organisationsstrukturen zur Integration sicherheitsrelevanter Anforderungen und Benennung von Zuständigen; ORP.5.A2 ergänzt die Beachtung der identifizierten Anforderungen in Planung, Konzeption und Umsetzung sowie die Festlegung von Verantwortlichkeiten und Korrekturmaßnahmen. Damit ist das geforderte Verfahren zur Sammlung, Integration und Priorisierung der Rahmenbedingungen inhaltlich abgedeckt.
- **Lücken:** [gpt-5.4-mini] Die GS++-Anforderung nennt zusätzlich explizit Priorisierung und Verankerung eines Verfahrens auf Governance-Ebene. Diese Punkte sind in den Kandidaten nur implizit bzw. nicht so explizit formuliert, werden jedoch durch die Kombination der genannten Anforderungen praktisch mit abgedeckt.

### GC.7.1.2 — Anhörung zuständiger Stellen
- **Confidence:** 0.42
- **Gemappte GS-Anforderungen:**
  - `DER.2.1.A4` [Basis] Benachrichtigung betroffener Stellen bei Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `DER.2.2.A1` [Basis] Prüfung rechtlicher und regulatorischer Rahmenbedingungen zur Erfassung und Auswertbarkeit — _DER.2.2 Vorsorge für die IT-Forensik_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.1.A4=0.42, DER.2.2.A1=0.42, ORP.5.A4=0.42
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8400 gs_ids=ORP.5.A4;DER.2.1.A4;DER.2.2.A1
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A4 passt inhaltlich am ehesten, weil dort der Prozess zur Identifikation relevanter gesetzlicher, vertraglicher und sonstiger Vorgaben im Compliance Management beschrieben wird. Die GS++-Anforderung GC.7.1.2 geht jedoch darüber hinaus und verlangt ausdrücklich, die für die Einhaltung gesetzlicher Verpflichtungen zuständigen Stellen in der Institution anzuhören; dieser Konsultationsaspekt ist in ORP.5.A4 nicht explizit enthalten. DER.2.1.A4 und DER.2.2.A1 enthalten ebenfalls die Einbeziehung bestimmter Stellen wie Datenschutzbeauftragte, Betriebs-/Personalrat oder Rechtsabteilung bei Vorfällen bzw. forensischen Maßnahmen. Das zeigt eine ähnliche organisatorische Einbindung zuständiger Stellen, deckt aber nur spezielle Anlässe und nicht allgemein die Anhörung bei der Dokumentation von Compliance-Verpflichtungen ab.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind der allgemeine, präventive Anhörungs-/Abstimmungsprozess mit zuständigen Stellen zur Dokumentation von Compliance-Verpflichtungen sowie die breite institutionelle Beteiligung über die in den Kandidaten genannten Spezialfälle hinaus. Die Kandidaten adressieren Identifikation von Vorgaben bzw. Einbindung bei Vorfällen/Forensik, aber nicht ausdrücklich die geforderte Anhörung zuständiger Stellen im Compliance-Management-Verfahren.

### GC.8.1.1.1.1 — Vorspracherecht des Informationssicherheitsbeauftragten
- **Confidence:** 0.93
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A12` [Standard] Management-Berichte zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** ISMS.1.A4 passt am ehesten, weil dort ausdrücklich geregelt ist, dass die Institutionsleitung dem oder der ISB die Möglichkeit einräumen MUSS, bei Bedarf direkt an sie selbst zu berichten. Das trifft den Kern eines direkten Zugangs zur Leitung, jedoch nur als 'bei Bedarf' und nicht als ausdrücklich verankertes Vorspracherecht. ISMS.1.A1 ergänzt dies, da die Institutionsleitung regelmäßig über den Status der Informationssicherheit informiert werden MUSS und sich insbesondere über Risiken und Konsequenzen informieren lassen MUSS; damit wird die Leitungsinformation abgesichert, aber ebenfalls kein formales Vorspracherecht des ISB geschaffen. ISMS.1.A12 beschreibt regelmäßige Management-Berichte des oder der ISB an die Institutionsleitung und damit einen strukturierten Informationskanal an die Leitung, jedoch ohne die geforderte direkte, verankerte Vortrags- bzw. Vorsprachebefugnis. Zusammen decken die Anforderungen den Informationsfluss zur Leitung teilweise ab, nicht aber die explizite institutionelle Verankerung eines direkten Vorspracherechts des ISB.
- **Lücken:** Nicht abgedeckt ist die explizite, verbindliche Verankerung eines direkten Vorspracherechts des ISB bei der Institutionsleitung als eigenständige organisatorische Regelung. Die Kandidaten regeln nur Berichtsmöglichkeit, regelmäßige Information oder Management-Berichte, nicht aber ein formales Vorrang-/Direktvorspracherecht unabhängig von Bedarf, Berichtsrhythmus oder Berichtskanal.

## Keine Abdeckung (2)

### GC.3.2 — Analyse der internen interessierten Parteien
- **Confidence:** 0.48
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9700 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidatenanforderungen behandelt die inhaltliche Pflicht, ein Verfahren zum Ermitteln aller internen interessierten Parteien sowie deren Bedürfnisse und Erwartungen an das Informationssicherheitsmanagement zu verankern. Die Kandidaten adressieren stattdessen Compliance-Prüfungen, rechtliche Rahmenbedingungen, Vorfallbehandlung, Administration, Netzwerk-/Systemthemen oder Outsourcing-Richtlinien. Das ist weder inhaltlich noch regelungsseitig eine passende Entsprechung zur Stakeholder-Analyse im ISMS.
- **Lücken:** [gpt-5.4-mini] Es fehlt ein Verfahren zur systematischen Ermittlung interner interessierter Parteien (z. B. Geschäftsführung, Mitarbeitende, Führungskräfte, Betriebs-/Personalrat) und zur Erfassung ihrer Bedürfnisse und Erwartungen an das Informationssicherheitsmanagement. Auch Anforderungen zur Dokumentation, Aktualisierung oder Auswertung dieser Stakeholder-Bedarfe sind in den Kandidaten nicht enthalten.

### GC.5.1.1 — Festlegung der Geschäftsprozesse
- **Confidence:** 0.48
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9600 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidatenanforderungen deckt die geforderte Festlegung der für den Geltungsbereich relevanten Geschäftsprozesse inhaltlich ab. ORP.5.A4 und ORP.5.A8 behandeln Compliance-Management und dessen Überprüfung, nicht die systematische Ermittlung bzw. Festlegung von Geschäftsprozessen. OPS.1.1.1.A12 und OPS.1.1.3.A7 beziehen sich auf Betriebs- bzw. Änderungsprozesse in der IT, nicht auf die Geschäftsprozesslandschaft der Institution. DER.4.A3 und DER.4.A7 betreffen den Geltungsbereich bzw. kritische Geschäftsprozesse im Notfallmanagement, was thematisch zu eng und anders ausgerichtet ist. Die übrigen Kandidaten sind fachlich noch weiter entfernt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt ist die eigentliche organisatorische Festlegung/Benennung der relevanten Geschäftsprozesse für einen Scope. Die Kandidaten adressieren höchstens angrenzend Prozessdokumentation, Compliance, Betrieb oder Notfallmanagement, aber nicht die gewünschte grundlegende Prozesslandkarte bzw. Prozessauswahl.
