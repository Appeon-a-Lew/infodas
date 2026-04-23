# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:42:40

**Gesamt:** 8 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 6 |
| Keine Abdeckung | 2 |

## Teilweise abgedeckt (6)

### GC.2.1 — Festlegung des externen Kontextes der Institution
- **Confidence:** 0.45
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A2` [Basis] Festlegung der Sicherheitsziele und -strategie — _ISMS.1 Sicherheitsmanagement_
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ISMS.1.A2=0.45, ORP.5.A1=0.45, ORP.5.A4=0.45
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8900 gs_ids=ORP.5.A1;ORP.5.A4;ISMS.1.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A1 und ORP.5.A4 decken den Teil der Anforderung ab, der die Identifikation, Sammlung und Verarbeitung gesetzlicher, vertraglicher und sonstiger relevanter Vorgaben für das Informationssicherheitsmanagement verlangt. ISMS.1.A2 ergänzt dies insofern, als dort die Festlegung und Dokumentation der Sicherheitsziele und der Sicherheitsstrategie sowie deren Überprüfung gefordert wird. Zusammen passt das organisatorisch zum Thema Kontext-/Rahmenbedingungenanalyse, aber die GS++-Anforderung geht darüber hinaus: Sie verlangt ausdrücklich die systematische Analyse, Integration und Priorisierung aller externen Kontextfaktoren wie gesellschaftliche, technologische, wirtschaftliche und ökologische Bedingungen, nicht nur rechtliche/vertragliche Vorgaben oder allgemeine Sicherheitsziele.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die explizit genannten externen Kontextfaktoren außerhalb von Recht/Vertrag, insbesondere gesellschaftliche und kulturelle Faktoren, technologische Entwicklungen, wirtschaftliche Marktbedingungen sowie ökologische und physische Umweltbedingungen. Ebenfalls fehlt die explizite Priorisierung aller externen Rahmenbedingungen als Verfahren.

### GC.3.1 — Analyse der externen interessierten Parteien
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A2=0.47, ORP.5.A4=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9300 gs_ids=ORP.5.A4;ORP.5.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A4 passt inhaltlich am besten, weil die Anforderung ausdrücklich einen Prozess verlangt, um relevante gesetzliche, vertragliche und sonstige Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement zu identifizieren. Damit wird der Kern der Ermittlung externer interessierter Parteien und ihrer sicherheitsrelevanten Anforderungen teilweise adressiert, jedoch nicht die systematische Ermittlung aller externen Parteien selbst. ORP.5.A2 ergänzt dies, da dort sicherheitsrelevante Anforderungen bei Planung, Konzeption und Beschaffung berücksichtigt und Maßnahmen zur Vermeidung von Verstößen festgelegt werden müssen; das deckt die Verarbeitung identifizierter Anforderungen ab, aber ebenfalls nicht die vollständige Stakeholder-Analyse. Beide Anforderungen bleiben auf rechtliche/vertragliche Vorgaben und deren Behandlung fokussiert und ersetzen nicht das geforderte Verfahren zur Identifikation aller externen interessierten Parteien samt Bewertung ihrer Bedürfnisse, Erwartungen und Priorisierung.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die explizite Ermittlung aller externen interessierten Parteien (z. B. Kunden, Dienstleister, Öffentlichkeit), die systematische Bewertung ihrer Bedürfnisse/Erwartungen, die Priorisierung der Anforderungen sowie die Entscheidung, welche Anforderungen als verbindliche Verpflichtungen ins ISMS übernommen werden. Die Kandidaten behandeln primär Compliance-/Vorgabenmanagement, nicht die Stakeholder-Analyse als solchen.

### GC.5.1.1 — Festlegung der Geschäftsprozesse
- **Confidence:** 0.43
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.1.A12` [Standard] Spezifikation und Umsetzung klarer Betriebsprozesse — _OPS.1.1.1 Allgemeiner IT-Betrieb_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.1.A12=0.43
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.8600 gs_ids=OPS.1.1.1.A12
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.1.A12 passt inhaltlich am besten, weil dort für alle Aufgaben Betriebsprozesse spezifiziert werden sollen und explizit festgelegt wird, welche Tätigkeiten, Abhängigkeiten sowie organisatorischen Schnittstellen es gibt. Das trifft den Kern der GS++-Anforderung GC.5.1.1, nämlich relevante Geschäftsprozesse für den Geltungsbereich festzulegen. Allerdings geht GC.5.1.1 stärker auf die Auswahl bzw. Festlegung der relevanten Geschäftsprozesse im Rahmen der Informationssicherheitseinstufung ein, während OPS.1.1.1.A12 allgemeine IT-Betriebsprozesse beschreibt und nicht die unternehmensweite Relevanzbestimmung von Geschäftsprozessen fordert.
- **Lücken:** [gpt-5.4-mini] Nicht vollständig abgedeckt sind die domänenspezifische Festlegung der für den Geltungsbereich relevanten Geschäftsprozesse im Sinne der Informationssicherheitseinstufung sowie der Bezug auf bestehende Prozesslandkarten/Managementsysteme als Ausgangsbasis. Die Anforderung bleibt zudem auf Betriebsprozesse fokussiert und deckt die allgemeinere Governance-Perspektive nur teilweise ab.

### GC.6.1.4 — Freigabe der Sicherheitsleitlinie
- **Confidence:** 0.49
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** Gemittelte Kandidatenscores: ISMS.1.A3=0.49
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9800 gs_ids=ISMS.1.A3
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ISMS.1.A3 deckt die Kernanforderung direkt ab: Beide Anforderungen verlangen, dass die Institutionsleitung eine Sicherheitsleitlinie bzw. Leitlinie zur Informationssicherheit verabschiedet/autorisieren muss. Die GS++-Anforderung fokussiert explizit auf die Freigabe durch die Institutionsleitung; ISMS.1.A3 enthält genau diese Freigabe-/Verabschiedungspflicht durch die Institutionsleitung sowie die inhaltliche Ausgestaltung der Leitlinie.

### GC.7.1 — Verfahren und Regelungen
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A1=0.48, ORP.5.A2=0.48, ORP.5.A4=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9600 gs_ids=ORP.5.A4;ORP.5.A1;ORP.5.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Grundschutz-Anforderungen ORP.5.A4, ORP.5.A1 und ORP.5.A2 decken die GS++-Anforderung GC.7.1 inhaltlich vollständig ab. ORP.5.A1 verlangt die Identifikation und Dokumentation aller gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement. ORP.5.A4 ergänzt dies um den Prozess, alle relevanten Vorgaben zu identifizieren, geeignete Prozesse und Organisationsstrukturen aufzubauen und die Anforderungen in das Compliance Management zu integrieren. ORP.5.A2 deckt die Beachtung der identifizierten Anforderungen in Planung, Konzeption und Umsetzung sowie die Festlegung von Verantwortlichkeiten und Korrekturmaßnahmen ab. Damit werden Sammlung, Integration und organisatorische Verankerung der relevanten Rahmenbedingungen vollständig abgebildet.
- **Lücken:** [gpt-5.4-mini] Keine wesentlichen Lücken gegenüber der GS++-Anforderung; die Aspekte Sammlung, Integration, Priorisierung im Verfahren sowie die organisatorische Umsetzung sind durch die Kombination der drei Anforderungen abgedeckt.

### GC.8.1.1.1.1 — Vorspracherecht des Informationssicherheitsbeauftragten
- **Confidence:** 0.91
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A12` [Standard] Management-Berichte zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `DER.3.2.A9` [Standard] Integration in den Informationssicherheitsprozess — _DER.3.2 Revisionen auf Basis des Leitfadens IS-Revision_
- **Begründung:** ISMS.1.A4 passt am ehesten, weil dort die Möglichkeit geregelt ist, dass die Institutionsleitung dem oder der ISB erlaubt, bei Bedarf direkt an sie selbst zu berichten. Das ist dem Vorspracherecht inhaltlich nah, aber nicht gleichbedeutend mit einem ausdrücklich verankerten direkten Vorspracherecht des ISB. ISMS.1.A1 ergänzt dies, da die Institutionsleitung sich regelmäßig über den Status der Informationssicherheit informieren lassen muss und die Zuständigkeiten festzulegen sind; auch das unterstützt die direkte Berichts- und Eskalationsbeziehung, regelt aber kein explizites Vorspracherecht. ISMS.1.A12 fordert regelmäßige Management-Berichte an die Institutionsleitung und deckt damit den Informationsfluss zur Leitung ab, jedoch ebenfalls ohne das konkrete Recht des ISB, selbst direkt vorsprechen zu dürfen. DER.3.2.A9 verlangt, dass die Ergebnisse von IS-Revisionen sowie die Qualitätsverbesserungen in den regelmäßigen Bericht des oder der ISB an die Institutionsleitung aufgenommen werden; auch hier geht es um Berichterstattung an die Leitung, nicht um ein direktes Vorspracherecht. Zusammen decken die Kandidaten den Kontext der direkten Informationsweitergabe an die Institutionsleitung ab, aber das explizite organisatorische Recht des ISB, ohne Zwischenschaltung direkt bei der Leitung vorzusprechen, wird nicht vollständig normiert.
- **Lücken:** Nicht abgedeckt ist die ausdrückliche Verankerung eines direkten Vorspracherechts des ISB als eigenständiges Recht/Kompetenz gegenüber der Institutionsleitung. Die Kandidaten regeln nur Berichtspflichten, direkte Berichtsmöglichkeit oder regelmäßige Information der Leitung, aber nicht die verbindliche, formale Vorab-Sprech- bzw. Vortragsbefugnis des ISB. Daher fehlt der normative Grad der Forderung sowie die explizite rechtliche Absicherung dieses Zugangs.

## Keine Abdeckung (2)

### GC.3.2 — Analyse der internen interessierten Parteien
- **Confidence:** 0.48
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9700 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidatenanforderungen adressiert die geforderte systematische Ermittlung aller internen interessierten Parteien und ihrer Bedürfnisse/Erwartungen an das Informationssicherheitsmanagement. Die Kandidaten zu ORP.5 betreffen Compliance-Management, rechtliche Rahmenbedingungen oder dessen Überprüfung, aber nicht Stakeholder-Analyse im Sinne der GC.3.2-Anforderung. Andere Kandidaten behandeln Vorfälle, Fernwartung, Administration, Verschlüsselung oder Outsourcing und sind thematisch ebenfalls nicht passend.
- **Lücken:** [gpt-5.4-mini] Es fehlt eine Anforderung zur strukturierten Identifikation interner interessierter Parteien (z. B. Geschäftsführung, Mitarbeitende, Führungskräfte, Betriebs-/Personalrat) sowie zur Ermittlung und Pflege ihrer Bedürfnisse und Erwartungen an das ISMS.

### GC.7.1.2 — Anhörung zuständiger Stellen
- **Confidence:** 0.48
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9600 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidaten beschreibt inhaltlich die Anhörung zuständiger Stellen bei der Dokumentation von Compliance-Verpflichtungen. ORP.5.A4 behandelt die Identifikation rechtlicher Rahmenbedingungen und den Aufbau von Compliance-Prozessen, aber nicht die explizite Beteiligung von Rechtsabteilung, Datenschutz- oder anderen Fachstellen. DER.2.1.A4 und DER.2.2.A1 regeln die Einbeziehung bestimmter Stellen bei Sicherheitsvorfällen bzw. forensischen Untersuchungen, was thematisch und vom Anlass her abweicht. Die übrigen Kandidaten betreffen Überprüfung, Dokumentation, Revision, Outsourcing oder allgemeine Regelkonformität, nicht die vorgesehene Anhörung zuständiger Stellen zur Compliance-Dokumentation.
- **Lücken:** [gpt-5.4-mini] Es fehlt die konkrete Forderung, die für die Einhaltung gesetzlicher Verpflichtungen zuständigen internen Stellen vor bzw. im Rahmen der Erfassung von Compliance-Verpflichtungen anzuhören. Abgedeckt werden nur angrenzende Themen wie Identifikation von Compliance-Anforderungen, Informationspflichten bei Vorfällen oder allgemeine Dokumentation/Revision.
