# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini+manual:gspp_compliance_v3approach`)

Erzeugt: 2026-04-22T10:44:33

**Gesamt:** 8 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 0 |
| Teilweise abgedeckt | 7 |
| Keine Abdeckung | 1 |

## Teilweise abgedeckt (7)

### GC.2.1 — Festlegung des externen Kontextes der Institution
- **Confidence:** 0.47
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A2` [Basis] Festlegung der Sicherheitsziele und -strategie — _ISMS.1 Sicherheitsmanagement_
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ISMS.1.A2=0.47, ORP.5.A1=0.47, ORP.5.A4=0.47
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.9300 gs_ids=ORP.5.A1;ORP.5.A4;ISMS.1.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A1 passt inhaltlich, weil dort die Identifikation und Dokumentation aller gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement gefordert wird. ORP.5.A4 ergänzt dies, weil ein Prozess zur Identifikation relevanter Vorgaben sowie deren Einordnung im Compliance Management aufgebaut werden soll. ISMS.1.A2 passt ergänzend, da dort die Festlegung und regelmäßige Überprüfung der Sicherheitsziele und der Informationssicherheitsstrategie verlangt wird. Zusammen decken diese Anforderungen den Teil der GS++-Anforderung ab, der sich auf rechtliche und organisatorische Rahmenbedingungen sowie deren Verankerung im ISMS bezieht.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind wesentliche Teile des externen Kontextes wie gesellschaftliche und kulturelle Faktoren, technologische Entwicklungen, wirtschaftliche Bedingungen sowie ökologische und physische Umweltbedingungen. Die Kandidaten fokussieren primär auf rechtliche/vertragliche Vorgaben und ISMS-Strategie, nicht auf die umfassende Kontextanalyse und Priorisierung externer Einflussfaktoren.

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
[gpt-5.4-mini] ORP.5.A4 und ORP.5.A2 decken den Kernaspekt der Anforderung ab, nämlich das Identifizieren und Berücksichtigen relevanter externer bzw. rechtlich/vertraglicher Anforderungen für das Informationssicherheitsmanagement. ORP.5.A4 fordert ausdrücklich einen Prozess zur Identifikation aller relevanten gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement. ORP.5.A2 verlangt, dass sicherheitsrelevante Anforderungen bei Planung und Konzeption berücksichtigt und geeignete Maßnahmen zur Vermeidung von Verstößen umgesetzt werden. Damit ist die Aufnahme und Behandlung externer Verpflichtungen im ISMS teilweise abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die ausdrücklich geforderte systematische Ermittlung aller externen interessierten Parteien selbst sowie deren Bedürfnisse und Erwartungen, inklusive Bewertung von Relevanz und Priorität über reine rechtliche/vertragliche Vorgaben hinaus. Auch die explizite Festlegung, welche identifizierten Anforderungen als verbindliche Verpflichtungen ins ISMS aufgenommen werden, wird nur indirekt, nicht vollständig beschrieben.

### GC.5.1.1 — Festlegung der Geschäftsprozesse
- **Confidence:** 0.38
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.1.A12` [Standard] Spezifikation und Umsetzung klarer Betriebsprozesse — _OPS.1.1.1 Allgemeiner IT-Betrieb_
- **Begründung:** Gemittelte Kandidatenscores: OPS.1.1.1.A12=0.38
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.7600 gs_ids=OPS.1.1.1.A12
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] OPS.1.1.1.A12 passt inhaltlich am ehesten, weil dort für alle Aufgaben Betriebsprozesse spezifiziert werden sollen und die organisatorischen Schnittstellen sowie Zuständigkeiten festzulegen sind. Das berührt die allgemeine Festlegung von Prozessen, die für den Geltungsbereich relevant sind. Die GS++-Anforderung GC.5.1.1 verlangt jedoch spezifisch die Festlegung der Geschäftsprozesse auf Governance-/Compliance-Ebene als Grundlage der Informationssicherheitseinstufung; diese Ebene der prozessualen Auswahl und Abgrenzung wird durch OPS.1.1.1.A12 nur allgemein und nicht explizit abgedeckt.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die spezifische Governance-/Compliance-Perspektive, die explizite Auswahl der für den Geltungsbereich relevanten Geschäftsprozesse sowie der Bezug zur Informationssicherheitseinstufung. Die Anforderung aus OPS.1.1.1.A12 ist allgemeiner IT-Betriebsbezug und ersetzt keine institutionelle Prozesslandkarte bzw. fachliche Prozessfestlegung.

### GC.6.1.4 — Freigabe der Sicherheitsleitlinie
- **Confidence:** 0.49
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** Gemittelte Kandidatenscores: ISMS.1.A3=0.49
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9900 gs_ids=ISMS.1.A3
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Die Anforderung GC.6.1.4 verlangt, dass die festgelegte Sicherheitsleitlinie durch die Institutionsleitung autorisiert wird. ISMS.1.A3 deckt dies inhaltlich direkt ab, da dort gefordert wird, dass die Institutionsleitung eine übergeordnete Leitlinie zur Informationssicherheit verabschiedet. Die Verabschiedung durch die Leitung entspricht der geforderten Autorisierung. Weitere Kandidaten sind dafür nicht erforderlich.

### GC.7.1 — Verfahren und Regelungen
- **Confidence:** 0.48
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: ORP.5.A1=0.48, ORP.5.A2=0.48, ORP.5.A4=0.48
Model-Entscheidungen:
[gpt-5.4-mini] coverage=voll confidence=0.9700 gs_ids=ORP.5.A4;ORP.5.A1;ORP.5.A2
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A1 deckt die Identifikation und Dokumentation aller gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement ab. ORP.5.A4 ergänzt dies um einen Prozess zur Identifikation relevanter Vorgaben, die Festlegung von Zuständigen sowie die Integration sicherheitsrelevanter Anforderungen in das Compliance Management und die Kontrolle der Umsetzung. ORP.5.A2 deckt die Beachtung der identifizierten Anforderungen in Planung, Konzeption und Beschaffung sowie die Festlegung von Verantwortlichkeiten und Korrekturmaßnahmen ab. Zusammen bilden ORP.5.A1, ORP.5.A4 und ORP.5.A2 das geforderte Verfahren zur Sammlung, Integration und Priorisierung von Rahmenbedingungen für das Informationssicherheitsmanagement inhaltlich vollständig ab.
- **Lücken:** [gpt-5.4-mini] Keine wesentlichen Lücken gegenüber der GS++-Anforderung erkennbar; die Anforderungen zur Priorisierung werden zwar nicht wortgleich genannt, sind aber durch den beschriebenen Prozess zur Integration, Verantwortungszuordnung und Umsetzung ausreichend mitabgedeckt.

### GC.7.1.2 — Anhörung zuständiger Stellen
- **Confidence:** 0.21
- **Gemappte GS-Anforderungen:**
  - `DER.2.1.A4` [Basis] Benachrichtigung betroffener Stellen bei Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `DER.2.2.A1` [Basis] Prüfung rechtlicher und regulatorischer Rahmenbedingungen zur Erfassung und Auswertbarkeit — _DER.2.2 Vorsorge für die IT-Forensik_
  - `OPS.2.3.A10` [Standard] Etablierung einer zuständigen Person für das Auslagerungsmanagement — _OPS.2.3 Nutzung von Outsourcing_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Gemittelte Kandidatenscores: DER.2.1.A4=0.21, DER.2.2.A1=0.21, OPS.2.3.A10=0.21, ORP.5.A4=0.21
Model-Entscheidungen:
[gpt-5.4-mini] coverage=teilweise confidence=0.4200 gs_ids=ORP.5.A4;DER.2.1.A4;DER.2.2.A1;OPS.2.3.A10
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] ORP.5.A4 passt nur teilweise, weil es die Identifikation relevanter gesetzlicher und sonstiger Vorgaben im Compliance-Management beschreibt, aber nicht die konkrete Anhörung zuständiger Stellen. DER.2.1.A4 und DER.2.2.A1 sind nur insoweit verwandt, als dort bei Vorfällen bzw. forensischen Maßnahmen bestimmte Stellen wie Datenschutzbeauftragte oder Rechtsabteilung einzubeziehen sind; auch das ist jedoch nicht die allgemeine Anhörung bei der Dokumentation von Compliance-Verpflichtungen. OPS.2.3.A10 erwähnt die Einbeziehung in Vertragsgestaltung und Kommunikation, betrifft aber Auslagerungsmanagement und nicht das hier geforderte Anhören zuständiger Stellen für gesetzliche Verpflichtungen in der Informationsverarbeitung.
- **Lücken:** [gpt-5.4-mini] Nicht abgedeckt sind die eigentliche systematische Anhörung zuständiger fachlich zuständiger Stellen vor bzw. bei der Dokumentation von Compliance-Verpflichtungen sowie der allgemeine Compliance-Bezug über konkrete Melde-, Vorfall- oder Outsourcing-Situationen hinaus. Die genannten Kandidaten adressieren eher Identifikation, Einbezug in Einzelfällen oder organisatorische Zuständigkeiten, nicht die explizite Anhörung als Verfahren.

### GC.8.1.1.1.1 — Vorspracherecht des Informationssicherheitsbeauftragten
- **Confidence:** 0.88
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A12` [Standard] Management-Berichte zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `DER.3.2.A9` [Standard] Integration in den Informationssicherheitsprozess — _DER.3.2 Revisionen auf Basis des Leitfadens IS-Revision_
- **Begründung:** ISMS.1.A4 passt am ehesten, weil es der Institutionsleitung ausdrücklich vorschreibt, dem oder der ISB die Möglichkeit einzuräumen, bei Bedarf direkt an sie selbst zu berichten. Das trifft den Kern eines direkten Vorspracherechts, geht aber nicht so weit, dieses als explizites, organisatorisch verankertes Recht zu formulieren. ISMS.1.A1 ergänzt dies, da die Institutionsleitung sich regelmäßig über den Status der Informationssicherheit informieren lassen muss und Zuständigkeiten festlegt; auch hier wird jedoch kein direktes Vorspracherecht des ISB gefordert. ISMS.1.A12 verlangt Management-Berichte an die Institutionsleitung und stützt damit die direkte Berichtsbeziehung, regelt aber ebenfalls nicht das formale Vorspracherecht. DER.3.2.A9 enthält ebenfalls einen regelmäßigen Bericht des oder der ISB an die Institutionsleitung und ist damit inhaltlich verwandt, adressiert jedoch primär die Einbindung von Revisionsergebnissen in den Bericht und nicht das Vorspracherecht selbst.
- **Lücken:** Nicht abgedeckt ist die explizite, verbindliche Verankerung eines direkten Vorspracherechts des ISB als organisatorisches Recht gegenüber der Institutionsleitung. Die Kandidaten regeln nur direkte Berichtsmöglichkeit bzw. regelmäßige Berichte, aber nicht die formale Vorrang-/Zugangsregelung gegen mögliche Filterung durch andere Organisationseinheiten.

## Keine Abdeckung (1)

### GC.3.2 — Analyse der internen interessierten Parteien
- **Confidence:** 0.49
- **Begründung:** Kein GS-Kandidat wurde von den kombinierten Modellen ausgewählt.
Model-Entscheidungen:
[gpt-5.4-mini] coverage=keine confidence=0.9800 gs_ids=
[manual:gspp_compliance_v3approach] coverage=keine confidence=0.0000 gs_ids=
Model-Begründungen:
[gpt-5.4-mini] Keine der Kandidatenanforderungen behandelt das systematische Ermitteln interner interessierter Parteien und deren Bedürfnisse/Erwartungen an das Informationssicherheitsmanagement. ORP.5.A4 und ORP.5.A8 beziehen sich auf Compliance-Management, rechtliche Vorgaben und deren Überprüfung, nicht auf Stakeholder-Analyse. Die übrigen Kandidaten betreffen ebenfalls andere Themen wie Forensik, Vorfälle, Administration, Outsourcing, Datenbanken, DNS, Mobile Devices oder Fernwartung.
- **Lücken:** [gpt-5.4-mini] Es fehlt die explizite Pflicht, interne interessierte Parteien zu identifizieren und ihre Bedürfnisse und Erwartungen an das ISMS zu erfassen; auch die genannten Beispiele (Geschäftsführung, Mitarbeitende, Führungskräfte, Betriebsrat/Personalrat) werden nicht abgedeckt.
