# GS++ → IT-Grundschutz Mapping (Model: `gpt-5.4-mini`)

Erzeugt: 2026-04-21T09:50:43

**Gesamt:** 36 GS++-Anforderungen

| Coverage | Anzahl |
|---|---|
| Voll abgedeckt | 8 |
| Teilweise abgedeckt | 27 |
| Keine Abdeckung | 1 |

## Voll abgedeckt (8)

### GC.6.1 — Festlegung von Zielen für die Informationssicherheit
- **Confidence:** 0.96
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** ISMS.1.A3 fordert, dass die Institutionsleitung eine Informationssicherheitsleitlinie verabschiedet, die Sicherheitsziele beschreibt und den Bezug dieser Sicherheitsziele zu den Geschäftszielen und Aufgaben der Institution erläutert. Damit ist die in GC.6.1 geforderte Festlegung konkreter Ziele für die Informationssicherheit auf Basis der Rahmenbedingungen inhaltlich am engsten abgedeckt. Zwar nennt GS++ zusätzlich ausdrücklich messbare und konkrete Ziele sowie Berücksichtigung interessierter Parteien und Kontext, aber die Kernforderung nach Zieldefinition im Rahmen der Leitlinie ist durch ISMS.1.A3 vollständig adressiert; die Messbarkeit ist eher Präzisierung als eigenständiger zusätzlicher Inhalt in der Kandidatenliste.
- **Lücken:** Die explizite Forderung nach messbaren, konkret quantifizierten Zielen sowie nach Berücksichtigung interessierter Parteien und des Kontexts wird in ISMS.1.A3 nicht ausdrücklich genannt. Für eine strenge Auslegung könnte daher nur eine teilweise Deckung angenommen werden; inhaltlich besteht jedoch die wesentliche Übereinstimmung über Sicherheitsziele mit Geschäftsbezug.

### GC.6.1.1 — Festlegung einer Sicherheitsstrategie
- **Confidence:** 0.97
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A2` [Basis] Festlegung der Sicherheitsziele und -strategie — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** GC.6.1.1 fordert die gemeinsame Festlegung einer grundlegenden Sicherheitsstrategie durch Governance/Compliance und Institutionsleitung. ISMS.1.A2 deckt dies unmittelbar ab, da die Institutionsleitung Sicherheitsziele sowie eine Strategie für Informationssicherheit festlegen und dokumentieren muss. ISMS.1.A3 ergänzt dies inhaltlich durch die übergeordnete Leitlinie, die die wichtigsten Aspekte der Sicherheitsstrategie und den Bezug zu den Sicherheitszielen beschreibt. Zusammen ist die geforderte Festlegung einer Sicherheitsstrategie vollständig abgedeckt.

### GC.6.1.2 — Verpflichtung der Institutionsleitung
- **Confidence:** 0.90
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A2` [Basis] Festlegung der Sicherheitsziele und -strategie — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `ORP.3.A1` [Basis] Sensibilisierung der Institutionsleitung für Informationssicherheit — _ORP.3 Sensibilisierung und Schulung zur Informationssicherheit_
- **Begründung:** Die Grundschutz++-Anforderung verlangt die formale Zuweisung bzw. Verpflichtung der Institutionsleitung inklusive Gesamtverantwortung, Festlegung und Überwachung von Sicherheitszielen, Förderung des ISMS sowie Unterstützung durch Ressourcen und Beteiligung. ISMS.1.A1 deckt die Übernahme der Gesamtverantwortung, Steuerung/Kontrolle, Vorbildfunktion und Ressourcenausstattung ab. ISMS.1.A2 deckt das Festlegen von Sicherheitszielen und -strategie sowie deren regelmäßige Überprüfung ab. ISMS.1.A3 deckt die Verabschiedung einer Sicherheitsleitlinie mit Sicherheitszielen, Bezug zu Organisationszielen und Organisationsstruktur ab. ISMS.1.A4 deckt die Benennung des ISB, dessen Förderung des ISMS sowie die Ressourcenausstattung und Berichtsmöglichkeit an die Leitung ab. ORP.3.A1 ergänzt die explizite Unterstützung der Leitung für Sicherheitsmaßnahmen und deren Vorbildrolle. Zusammen ist die inhaltliche Zielsetzung der GS++-Anforderung vollständig abgedeckt.
- **Lücken:** Keine wesentlichen Lücken; die formale 'Verpflichtung der Institutionsleitung' wird im klassischen Grundschutz nicht als eigener Begriff so benannt, die geforderten Inhalte sind jedoch über die genannten Anforderungen abgedeckt.

### GC.6.1.3 — Erstellung einer Sicherheitsleitlinie
- **Confidence:** 0.93
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A11` [Standard] Aufrechterhaltung der Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `ORP.3.A1` [Basis] Sensibilisierung der Institutionsleitung für Informationssicherheit — _ORP.3 Sensibilisierung und Schulung zur Informationssicherheit_
  - `OPS.1.2.4.A8` [Standard] Informationsfluss zwischen Mitarbeitenden und Institution — _OPS.1.2.4 Telearbeit_
- **Begründung:** GC.6.1.3 fordert die Festlegung einer für die Institution passenden Sicherheitsleitlinie als zentrales, an Mitarbeitende zu kommunizierendes Dokument mit Gesamtverantwortung der Leitung, Informationssicherheitszielen, Strategie, Rollen/Zuständigkeiten und kontinuierlicher Verbesserung. ISMS.1.A3 deckt die Erstellung, Verabschiedung, Inhalte (Stellenwert, Ziele, Sicherheitsstrategie, Organisationsstruktur, Geltungsbereich) und Kommunikation an alle Mitarbeitenden direkt ab. ISMS.1.A1 ergänzt die explizite Gesamtverantwortung der Leitung sowie die Festlegung von Zuständigkeiten. ISMS.1.A11 ergänzt die regelmäßige Überprüfung und Aktualisierung der Leitlinie und der Sicherheitsstruktur, was die kontinuierliche Verbesserung abbildet. ORP.3.A1 und OPS.1.2.4.A8 stützen die erforderliche Kommunikation/Sensibilisierung gegenüber Mitarbeitenden, sind aber nur flankierend relevant. Insgesamt ist die Grundschutz++-Anforderung inhaltlich vollständig abgedeckt.

### GC.6.1.4 — Freigabe der Sicherheitsleitlinie
- **Confidence:** 0.98
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** Die GS++-Anforderung verlangt, dass die festgelegte Sicherheitsleitlinie von der Institutionsleitung autorisiert wird. ISMS.1.A3 fordert inhaltlich genau dies: Die Institutionsleitung MUSS eine übergeordnete Leitlinie zur Informationssicherheit verabschieden. Damit ist die erforderliche Freigabe/Autorisation durch die Leitung direkt abgedeckt.

### GC.7.1 — Verfahren und Regelungen
- **Confidence:** 0.91
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** GC.7.1 fordert ein Verfahren zur Sammlung, Integration und Priorisierung aller für das ISMS relevanten Rahmenbedingungen. ORP.5.A1 deckt die Identifikation und Dokumentation aller gesetzlichen, vertraglichen und sonstigen Vorgaben ab. ORP.5.A4 ergänzt dies um den Aufbau eines Prozesses zur Identifikation relevanter Vorgaben sowie geeigneter Prozesse/Organisationsstrukturen zur Gewährleistung des Überblicks und zur Integration sicherheitsrelevanter Anforderungen. ORP.5.A2 deckt die Beachtung dieser identifizierten Anforderungen in Planung und Konzeption sowie die Festlegung von Zuständigkeiten und Maßnahmen zur Vermeidung/Behebung von Verstößen ab. Zusammengenommen wird damit der geforderte Verfahrens- und Regelungsrahmen inhaltlich vollständig abgedeckt.

### GC.8.1.1 — Festlegung von Rollen und Zuständigkeiten
- **Confidence:** 0.96
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A6` [Basis] Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** ISMS.1.A6 beschreibt eine übergreifende Organisationsstruktur für Informationssicherheit, in der Rollen definiert, qualifizierte Personen benannt und Aufgaben, Rollen, Verantwortungen und Kompetenzen nachvollziehbar zugewiesen werden müssen. Das deckt die GS++-Anforderung zur Festlegung von Rollen und Zuständigkeiten im ISMS inklusive Kompetenzen/Befugnissen inhaltlich direkt ab. Der Hinweis auf ausreichende Ressourcen und Vertretungsregelungen geht sogar darüber hinaus.

### GC.9.1.2 — Kommunikation im Projektmanagement
- **Confidence:** 0.93
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A9` [Basis] Integration der Informationssicherheit in organisationsweite Abläufe und Prozesse — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** GC.9.1.2 fordert bei sicherheitsrelevanten Projekten bzw. Projekten mit Auswirkungen auf die Informationsverarbeitung eine frühzeitige Beteiligung des ISB (und ggf. weiterer sicherheitsrelevanter Stellen) zu festgelegten Zeitpunkten im Projektverlauf. ISMS.1.A4 deckt dies direkt ab, da der ISB bei größeren Projekten sowie bei der Einführung neuer Anwendungen und IT-Systeme frühzeitig beteiligt werden MUSS. ISMS.1.A9 deckt den übergeordneten Grundsatz ab, dass der ISB bei sicherheitsrelevanten Entscheidungen ausreichend beteiligt werden MUSS und Informationssicherheit in neue Prozesse und Projekte zu integrieren ist. Zusammen ist die geforderte Beteiligung im Projektverlauf inhaltlich abgedeckt.
- **Lücken:** ISMS.1.A4 nennt keine explizit festgelegten Zeitpunkte wie Beschaffung oder vor Produktivsetzung; dieser Aspekt ist nur implizit durch 'frühzeitig' abgedeckt. Eine Beteiligung weiterer sicherheitsrelevanter Organe wird nicht konkretisiert.

## Teilweise abgedeckt (27)

### GC.1.1 — Errichtung und Aufrechterhaltung eines ISMS
- **Confidence:** 0.88
- **Gemappte GS-Anforderungen:**
  - `IND.1.A1` [Basis] Einbindung in die Sicherheitsorganisation — _IND.1 Prozessleit- und Automatisierungstechnik_
- **Begründung:** IND.1.A1 deckt den Kernaspekt der Errichtung eines ISMS ab, da es ausdrücklich fordert, dass für den OT-Betrieb ein ISMS als eigenständiges oder integriertes Managementsystem existieren MUSS. Damit ist die Existenz bzw. Etablierung eines ISMS inhaltlich getroffen. Die Grundschutz++-Anforderung verlangt jedoch zusätzlich die Verankerung von Verfahren und Regelungen zur Aufrechterhaltung des ISMS sowie die kontinuierliche Überprüfung und das Einleiten von Gegenmaßnahmen. Diese Aspekte werden durch IND.1.A1 nicht beschrieben.
- **Lücken:** Nicht abgedeckt sind die Anforderungen an die Aufrechterhaltung des ISMS: kontinuierliche Überprüfung der Einhaltung, Ableitung und Umsetzung von Gegenmaßnahmen sowie der Hinweis, dass die komplette Vorgehensweise mindestens einmal vollständig durchlaufen wurde. Auch die Verankerung konkreter Verfahren und Regelungen ist dort nicht ausgeführt.

### GC.10.1 — Festlegung von Vorgehensweisen
- **Confidence:** 0.92
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `DER.2.1.A7` [Standard] Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `DER.3.1.A5` [Standard] Integration in den Informationssicherheitsprozess — _DER.3.1 Audits und Revisionen_
- **Begründung:** GC.10.1 verlangt die Festlegung der ISMS-Verfahren und Zuständigkeiten sowie die Abdeckung mehrerer Verfahrensbereiche (Risiko, Änderungen, Dokumentenlenkung, Leistungsbewertung/Auditierung, kontinuierliche Verbesserung, reaktive Verfahren). ORP.5.A4 deckt die Festlegung von Zuständigkeiten und die organisatorische Verankerung des Compliance-Managements ab, aber nicht die ISMS-Verfahren insgesamt. DER.2.1.A7 deckt die Definition und Dokumentation eines reaktiven Verfahrens für Sicherheitsvorfälle ab. DER.3.1.A5 deckt Auditierung, Korrekturmaßnahmen und Rückfluss der Ergebnisse in den Informationssicherheitsprozess ab. Zusammen ergeben sich wichtige Teilaspekte, aber nicht alle geforderten Verfahrensarten der Grundschutz++-Anforderung.
- **Lücken:** Nicht abgedeckt sind insbesondere die allgemeine Festlegung sämtlicher ISMS-Verfahren als Gesamtpaket, die explizite Risikobetrachtung, die Dokumentenlenkung sowie die explizite Regelung der Etablierung von Änderungen im ISMS und die Leistungsbewertung außerhalb von Audit/Korrekturmaßnahmen. Ein einzelnes oder die ausgewählten GS-Anforderungen bilden daher nur einen Teil der Anforderung ab.

### GC.10.2 — Freigabe von Vorgehensweisen
- **Confidence:** 0.94
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A2` [Basis] Festlegung der Sicherheitsziele und -strategie — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** Die GS++-Anforderung verlangt, dass die Institutionsleitung die Verfahren des ISMS autorisiert/freigibt und diese Freigabe dokumentiert wird. ISMS.1.A1 deckt die Leitungsverantwortung für den Sicherheitsprozess ab, einschließlich Initiierung, Steuerung und Kontrolle sowie Informationssicherheit vorleben. ISMS.1.A2 deckt die Festlegung und Dokumentation von Sicherheitszielen und -strategie durch die Institutionsleitung ab. Beide Anforderungen liegen inhaltlich nahe an der erforderlichen Leitungsfreigabe für ISMS-Vorgehensweisen, enthalten aber keine explizite Freigabe einzelner ISMS-Verfahren durch die Institutionsleitung.
- **Lücken:** Es fehlt die explizite Anforderung, dass die Institutionsleitung die konkreten ISMS-Verfahren/Vorgehensweisen autorisiert oder freigibt und dass genau diese Freigabe dokumentiert wird. Die Kandidaten behandeln eher Gesamtverantwortung, Strategie und Rahmenvorgaben, nicht die formale Freigabe von Verfahren.

### GC.11.1 — Methodik für das Risikomanagement
- **Confidence:** 0.90
- **Gemappte GS-Anforderungen:**
  - `APP.7.A5` [Standard] Geeignete Steuerung der Anwendungsentwicklung — _APP.7 Entwicklung von Individualsoftware_
  - `CON.8.A16` [Standard] Geeignete Steuerung der Software-Entwicklung — _CON.8 Software-Entwicklung_
- **Begründung:** Die beiden Kandidaten decken den Kernaspekt einer festgelegten Risikomanagement-Methodik in Projekten bzw. der Softwareentwicklung ab. Beide Anforderungen verlangen ausdrücklich ein geeignetes Risikomanagement als Bestandteil eines Steuerungs-/Projektmanagementmodells. Damit ist die Existenz einer Methodik grundsätzlich adressiert. Die GS++-Anforderung geht jedoch weiter: Sie fordert eine einheitliche, institutionweit verankerte Methodik für das Informationssicherheitsrisikomanagement auf Basis von Kontext, Anforderungen interessierter Parteien und Risikozielen sowie verbindliche Kriterien für Risikoeinschätzung, -bewertung und -behandlung und die Rolle des Risikoeigentümers. Diese Breite und Verbindlichkeit wird von den Kandidaten nicht vollständig erreicht.
- **Lücken:** Es fehlen die institutionweite Verankerung, die Ableitung aus Kontext und Anforderungen interessierter Parteien, die explizite Festlegung einheitlicher Kriterien für Risikoeinschätzung/-bewertung/-behandlung sowie die Rolle des Risikoeigentümers. Die Kandidaten beziehen sich zudem nur auf einzelne Vorhaben/Entwicklungsprozesse, nicht auf das allgemeine Informationssicherheitsrisikomanagement.

### GC.2.1 — Festlegung des externen Kontextes der Institution
- **Confidence:** 0.86
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A1` [Basis] Identifikation der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ISMS.1.A2` [Basis] Festlegung der Sicherheitsziele und -strategie — _ISMS.1 Sicherheitsmanagement_
  - `INF.12.A1` [Basis] Auswahl geeigneter Kabeltypen — _INF.12 Verkabelung_
- **Begründung:** Die Anforderung verlangt ein Verfahren zur Sammlung, Integration und Priorisierung externer Rahmenbedingungen für das ISMS. ORP.5.A1 und ORP.5.A4 decken die Identifikation und Integration relevanter gesetzlicher, vertraglicher und sonstiger Vorgaben ab. ISMS.1.A2 adressiert die Festlegung und regelmäßige Überprüfung der Sicherheitsziele und -strategie auf Basis organisatorischer Rahmenbedingungen, was den Kontextbezug teilweise trifft. INF.12.A1 enthält die Berücksichtigung von Umgebungsbedingungen, jedoch nur für Kabeltypen und damit nur einen sehr engen Teilaspekt externer physischer Umweltbedingungen. Eine echte Abdeckung der geforderten systematischen Erfassung aller externen Faktoren einschließlich gesellschaftlicher, kultureller, technologischer, wirtschaftlicher sowie ökologischer und physischer Rahmenbedingungen findet sich in keinem Kandidaten vollständig.
- **Lücken:** Nicht abgedeckt sind insbesondere die explizite systematische Erfassung und Priorisierung aller externen Kontextfaktoren über rechtliche/vertragliche Vorgaben hinaus, also gesellschaftliche und kulturelle Faktoren, technologische Entwicklungen, wirtschaftliche Marktbedingungen sowie ökologische und physische Umweltbedingungen als allgemeiner ISMS-Kontext. Die Kandidaten fokussieren überwiegend auf Compliance, Strategie oder sehr spezifische Einzelfälle.

### GC.2.2 — Festlegung des internen Kontextes der Institution
- **Confidence:** 0.92
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A2` [Basis] Festlegung der Sicherheitsziele und -strategie — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** ISMS.1.A2 deckt den Kern der Anforderung ab, weil dort die Institutionsleitung Sicherheitsziele und eine Informationssicherheitsstrategie festlegen sowie konzeptionelle und organisatorische Rahmenbedingungen schaffen muss. Das entspricht dem geforderten Verfahren zur Festlegung des Kontexts auf oberster Ebene. Die GS++-Anforderung geht jedoch weiter und verlangt explizit ein Verfahren zur systematischen Sammlung, Integration und Priorisierung interner Rahmenbedingungen (z. B. Werte, Struktur, Prozesse, Infrastruktur, Kultur). Diese Kontextanalyse wird in ISMS.1.A2 nicht in dieser Tiefe gefordert.
- **Lücken:** Es fehlt die explizite Anforderung, interne Kontextfaktoren systematisch zu erfassen, zu integrieren und zu priorisieren. Insbesondere werden Werte/Kultur, Organisationsstruktur, Prozesse/Arbeitsabläufe und IT-Infrastruktur als zu analysierende Kontextbestandteile nicht ausdrücklich benannt.

### GC.3.1 — Analyse der externen interessierten Parteien
- **Confidence:** 0.93
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** ORP.5.A4 deckt den Kern der Anforderung ab, da dort ein Prozess zur Identifikation aller relevanten gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement gefordert wird. Das entspricht inhaltlich der Ermittlung externer interessierter Parteien bzw. deren Anforderungen zumindest insoweit, als deren Vorgaben als Compliance-Anforderungen erfasst werden. Die spezielle Forderung nach einem Verfahren zur Ermittlung aller externen interessierten Parteien samt ihrer Bedürfnisse und Erwartungen sowie deren Priorisierung und Überführung in verbindliche ISMS-Verpflichtungen wird jedoch nicht vollständig beschrieben.
- **Lücken:** Es fehlt die explizite Identifikation aller externen interessierten Parteien selbst (z. B. Kunden, Öffentlichkeit, Dienstleister) sowie die systematische Bewertung von Relevanz und Priorität ihrer Bedürfnisse/Erwartungen und die ausdrückliche Festlegung, welche Anforderungen als verbindliche Verpflichtungen ins ISMS aufgenommen werden.

### GC.4.1 — Festlegung des Geltungsbereichs
- **Confidence:** 0.93
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A3` [Basis] Erstellung einer Leitlinie zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** ISMS.1.A3 deckt die Kernaussage ab, dass für die Informationssicherheits-Leitlinie ein klarer Geltungsbereich festgelegt sein muss und diese von der Institutionsleitung verabschiedet wird. Damit ist die formale Scope-Festlegung der Grundschutz++-Anforderung inhaltlich getroffen. Die Anforderungen zu nachvollziehbarer Abgrenzung des gesamten ISMS-Scope nach Freigabe der Institutionsleitung sind jedoch nur teilweise beschrieben.
- **Lücken:** Nicht ausdrücklich abgedeckt sind die geforderte nachvollziehbare Abgrenzung des gesamten ISMS-Geltungsbereichs im Sinne einer detaillierten Scope-Definition (inkl. expliziter Einbeziehung/Ausschluss von Bereichen), die formale Festlegung nach Freigabe der Institutionsleitung für den ISMS-Scope sowie die konkrete Abgrenzung von Standorten, Systemen und externen Partnern/Dienstleistern.

### GC.5.1 — Vorgehen bei der Infomationssicherheitseinstufung
- **Confidence:** 0.83
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Die GS++-Anforderung verlangt ein Verfahren zur Festlegung von Geschäftsprozessen und zur Einstufung des Schutzbedarfs der dabei verarbeiteten Informationen. ORP.5.A2 deckt inhaltlich ab, dass sicherheitsrelevante Anforderungen bei der Planung und Konzeption von Geschäftsprozessen einfließen müssen. ORP.5.A4 adressiert den Aufbau von Prozessen zur Identifikation relevanter Vorgaben und zur Überführung sicherheitsrelevanter Anforderungen in Sicherheitsmaßnahmen. Beide zusammen treffen den Governance-/Prozessaspekt, aber nicht die explizite, systematische Schutzbedarfseinstufung von Geschäftsprozessen und Informationen.
- **Lücken:** Es fehlt die explizite Vorgabe eines förmlichen Verfahrens zur Schutzbedarfsermittlung/-einstufung für Geschäftsprozesse und die darin verarbeiteten Informationen sowie die klare Unterscheidung normal/hoch im prozessorientierten Ansatz.

### GC.5.1.1 — Festlegung der Geschäftsprozesse
- **Confidence:** 0.89
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.1.A12` [Standard] Spezifikation und Umsetzung klarer Betriebsprozesse — _OPS.1.1.1 Allgemeiner IT-Betrieb_
- **Begründung:** Die GS++-Anforderung verlangt, dass die für den Geltungsbereich relevanten Geschäftsprozesse festgelegt werden. OPS.1.1.1.A12 fordert, für alle Aufgaben Betriebsprozesse zu spezifizieren, inklusive Tätigkeiten, Abhängigkeiten, Initiierung, Umsetzung und Schnittstellen. Das ist die einzige Kandidatenanforderung, die inhaltlich die Festlegung von Prozessen im organisatorischen Sinne adressiert. Eine vollständige Abdeckung liegt jedoch nicht vor, da GS++ explizit die Festlegung relevanter Geschäftsprozesse im Rahmen der Informationssicherheitseinstufung fordert, nicht nur die Spezifikation von Betriebsprozessen.
- **Lücken:** Es fehlt die explizite Bezugnahme auf die Geschäftsprozesse des Geltungsbereichs bzw. auf den Schritt der Informationssicherheitseinstufung. OPS.1.1.1.A12 behandelt allgemein Betriebsprozesse des IT-Betriebs und nicht die Auswahl/Festlegung relevanter Geschäftsprozesse anhand eines Informationssicherheits-Kontexts.

### GC.5.1.2 — Festlegung des Schutzbedarfs
- **Confidence:** 0.92
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A2` [Basis] Festlegung der Sicherheitsziele und -strategie — _ISMS.1 Sicherheitsmanagement_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `SYS.3.2.2.A1` [Basis] Festlegung einer Strategie für das Mobile Device Management — _SYS.3.2.2 Mobile Device Management (MDM)_
- **Begründung:** Die Anforderung fordert die Festlegung des Schutzbedarfs relevanter Geschäftsprozesse und Informationsarten unter Berücksichtigung der Geschäftsziele und in Abstimmung mit der Institutionsleitung. ISMS.1.A2 deckt die Rolle der Institutionsleitung bei der Festlegung von Sicherheitszielen/-strategie und den organisatorischen Rahmen für den sicheren Umgang mit Informationen über alle Geschäftsprozesse ab. ORP.5.A4 ergänzt die Identifikation und Verarbeitung rechtlicher/sonstiger Vorgaben, die bei der Einstufung mitgedacht werden müssen. SYS.3.2.2.A1 enthält ausdrücklich die Grundsatzlogik, dass Strategien auf Basis des Schutzbedarfs der zu verarbeitenden Informationen festgelegt werden. Zusammen treffen die Kandidaten wesentliche Teile des Zielbilds, aber keine regelt die eigentliche Schutzbedarfsfeststellung mit den konkreten Einstufungsstufen 'normal'/'hoch', die Priorisierung des wichtigsten Geschäftsprozesses oder die explizite Entscheidung durch die Institutionsleitung zur Schutzbedarfseinstufung.
- **Lücken:** Es fehlt die konkrete Anforderung, den Schutzbedarf selbst systematisch für Geschäftsprozesse und Informationsarten festzulegen, einschließlich der Einstufung in 'normal' und 'hoch', der Priorisierung des wichtigsten Geschäftsprozesses sowie der expliziten Ableitung aus existenzbedrohenden Schäden bzw. besonders vertraulichen Informationen.

### GC.5.1.3 — Geschäftsprozesse mit hohem Schutzbedarf
- **Confidence:** 0.91
- **Gemappte GS-Anforderungen:**
  - `APP.2.2.A5` [Basis] Absicherung des Domänencontrollers — _APP.2.2 Active Directory Domain Services_
- **Begründung:** Einziger echter inhaltlicher Treffer ist APP.2.2.A5, da dort ausdrücklich eine Risikobetrachtung wegen der zentralen Rolle und Schadensauswirkung gefordert wird. Das trifft den Kern der geforderten dedizierten Risikobetrachtung für einen besonders schutzbedürftigen Bereich. Die übrigen Kandidaten behandeln allgemeines Compliance-, Organisations- oder Sicherheitsmanagement, aber nicht die spezifische risikobasierte Betrachtung von Geschäftsprozessen oder Informationsarten mit hohem Schutzbedarf als eigenständige Anforderung.
- **Lücken:** Abgedeckt ist nur die allgemeine Forderung nach einer Risikobetrachtung. Es fehlt die explizite Ausrichtung auf Geschäftsprozesse oder Informationsarten mit hohem Schutzbedarf sowie die Vorgabe, diese Risikobetrachtung dediziert und in einem separaten Dokument mit verbindlicher Risikomethodik zu dokumentieren.

### GC.7.1.1 — Gesetzliche Verpflichtungen
- **Confidence:** 0.95
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** ORP.5.A4 deckt den Kern der Anforderung ab, nämlich die Identifikation relevanter gesetzlicher Vorgaben und den Aufbau eines Prozesses, um diese für die Institution zu überblicken und zu berücksichtigen. Damit ist die geforderte Analyse gesetzlicher Verpflichtungen inhaltlich im Wesentlichen enthalten. Die spezifische Grundschutz++-Formulierung verlangt jedoch explizit die Analyse der gesetzlichen Verpflichtungen mit Bezug auf die Verarbeitung von Informationen; diese Fokussierung und die Dokumentation der Verpflichtungen werden in ORP.5.A4 nur allgemein adressiert.
- **Lücken:** Es fehlt die explizite Ausrichtung auf gesetzliche Verpflichtungen, die die Verarbeitung von Informationen betreffen, sowie die klare Forderung nach Dokumentation der identifizierten Verpflichtungen. ORP.5.A4 bleibt allgemeiner bei gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das IS-Management.

### GC.7.1.2 — Anhörung zuständiger Stellen
- **Confidence:** 0.78
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `DER.2.1.A4` [Basis] Benachrichtigung betroffener Stellen bei Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `DER.2.2.A1` [Basis] Prüfung rechtlicher und regulatorischer Rahmenbedingungen zur Erfassung und Auswertbarkeit — _DER.2.2 Vorsorge für die IT-Forensik_
- **Begründung:** Die GS++-Anforderung verlangt, dass für Compliance-Verpflichtungen zuständige Stellen innerhalb der Institution angehört werden. ORP.5.A4 deckt den Aufbau eines Compliance-Prozesses zur Identifikation relevanter rechtlicher Vorgaben und die Festlegung Zuständiger ab, aber nicht die explizite Anhörung von Fachstellen. DER.2.1.A4 und DER.2.2.A1 zeigen jeweils die Einbeziehung bzw. Prüfung von Rechtsabteilung, Datenschutzbeauftragten und weiteren Stellen bei rechtlichen Bewertungen; das entspricht inhaltlich dem Konsultationsaspekt. Insgesamt wird die Anhörung zuständiger Stellen jedoch nur indirekt und nur für Teilaspekte abgedeckt, nicht als allgemeine Regel für die Dokumentation aller Compliance-Verpflichtungen.
- **Lücken:** Es fehlt die explizite, allgemeine Vorgabe, dass die für gesetzliche Verpflichtungen in der Informationsverarbeitung zuständigen Stellen bereits bei der Dokumentation/Erfassung von Compliance-Verpflichtungen systematisch angehört werden. Die Kandidaten benennen nur einzelne Rollen oder nur anlassbezogene Einbeziehung, nicht die institutionalisierte Anhörung aller relevanten zuständigen Stellen.

### GC.7.1.3 — Vertragliche Verpflichtungen
- **Confidence:** 0.91
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `OPS.1.2.5.A19` [Standard] Fernwartung durch Dritte — _OPS.1.2.5 Fernwartung_
- **Begründung:** ORP.5.A4 deckt den allgemeinen Teil ab, dass relevante vertragliche Vorgaben im Compliance-Management identifiziert und berücksichtigt werden sollen. OPS.1.2.5.A19 deckt den spezifischen Fall vertraglicher Regelungen mit externen Wartungspersonen ab. Die GS++-Anforderung fordert jedoch ausdrücklich die Dokumentation einer Zusammenstellung aller vertraglichen Verpflichtungen, die die Informationsverarbeitung der Institution betreffen; dieser generelle Dokumentations-/Zusammenstellungsaspekt wird durch die Kandidaten nur indirekt bzw. nur für Teilbereiche adressiert.
- **Lücken:** Es fehlt die explizite Anforderung, alle vertraglichen Verpflichtungen mit Bezug zur Informationsverarbeitung institutionenweit zusammenzustellen und zu dokumentieren. ORP.5.A4 verlangt Identifikation/Übersicht über Vorgaben, aber nicht die dokumentierte Zusammenstellung solcher Verpflichtungen; OPS.1.2.5.A19 ist auf Fernwartung durch Dritte beschränkt.

### GC.7.1.4 — Prävention von Verstößen
- **Confidence:** 0.71
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A2` [Basis] Beachtung der Rahmenbedingungen — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `OPS.3.2.A8` [Standard] Erstellung einer Richtlinie für die Outsourcing-Dienstleistungen — _OPS.3.2 Anbieten von Outsourcing_
  - `OPS.2.3.A9` [Standard] Etablierung einer Richtlinie zur Auslagerung — _OPS.2.3 Nutzung von Outsourcing_
  - `OPS.1.1.6.A13` [Standard] Trennung der Testumgebung von der Produktivumgebung — _OPS.1.1.6 Software-Tests und -Freigaben_
  - `INF.14.A7` [Standard] Festlegung einer Sicherheitsrichtlinie für die GA — _INF.14 Gebäudeautomation_
- **Begründung:** Die GS++-Anforderung fordert allgemein Verfahren zur Prävention von Verstößen; die Guidance konkretisiert dies u. a. durch Schulungen, Berücksichtigung von Compliance-Verpflichtungen in Freigabe- und Testprozessen sowie eine konstruktive Fehlerkultur. Inhaltlich passend sind ORP.5.A2 (explizit Maßnahmen zur Vermeidung von Verstößen), OPS.3.2.A8 und OPS.2.3.A9 (Test- und Freigabeverfahren unter Berücksichtigung von Compliance-Risiken), OPS.1.1.6.A13 sowie INF.14.A7 (Vorgaben für Test/Freigabe bzw. Entwicklung und Test).
- **Lücken:** Nicht vollständig abgedeckt sind die explizit genannten Präventionsaspekte wie zielgruppengerechte Schulungen aller für Umsetzung und Einhaltung zuständigen Personen sowie die Förderung einer konstruktiven Fehlerkultur. Ein allgemeines Präventionsverfahren wird durch die Kandidaten nur indirekt bzw. für Teilaspekte gefordert.

### GC.8.1 — Verfahren zur Ressourcenplanung
- **Confidence:** 0.84
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A15` [Standard] Wirtschaftlicher Einsatz von Ressourcen für Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `OPS.1.1.1.A4` [Standard] Bereitstellen ausreichender Personal- und Sachressourcen — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `DER.3.1.A7` [Standard] Erstellung eines Auditprogramms — _DER.3.1 Audits und Revisionen_
- **Begründung:** Die GS++-Anforderung verlangt ein Verfahren zur kontinuierlichen und wirtschaftlichen Planung von Ressourcen für das ISMS inklusive personeller, finanzieller und materiell/technischer Ressourcen. ISMS.1.A15 deckt den wirtschaftlichen Einsatz sowie die Bezifferung und Bereitstellung von Ressourcen für Informationssicherheit ab. OPS.1.1.1.A4 adressiert die Planung ausreichender Personal- und Sachressourcen sowie die regelmäßige Anpassung der Ressourcenplanung. DER.3.1.A7 ergänzt dies um Reserven in der jährlichen Ressourcenplanung und einen kontinuierlichen Verbesserungsprozess. Zusammen sind wesentliche Inhalte abgedeckt, jedoch nicht explizit ein formales, ISMS-weites Verfahren für die kontinuierliche Gesamt-Ressourcenplanung über alle Ressourcenarten hinweg.
- **Lücken:** Nicht explizit abgedeckt ist ein verbindlich verankertes Verfahren zur kontinuierlichen ISMS-Ressourcenplanung als organisatorischer Prozess; außerdem fehlt die klare, vollständige Benennung aller drei Ressourcenarten in einem zusammenhängenden Anforderungskontext und die explizite ISMS-Bezugnahme für die materielle/technische sowie finanzielle Planung in einem einzigen Verfahren.

### GC.8.1.1.1 — Informationssicherheitsbeauftragter
- **Confidence:** 0.91
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `IND.1.A1` [Basis] Einbindung in die Sicherheitsorganisation — _IND.1 Prozessleit- und Automatisierungstechnik_
- **Begründung:** Die GS++-Anforderung fordert die Benennung eines Informationssicherheitsbeauftragten (ISB) mit unmittelbarer Unterstellung unter die Institutionsleitung sowie die operative Koordination der Informationssicherheit. ISMS.1.A4 deckt die Benennung des ISB, die Förderung der Informationssicherheit und die Mitsteuerung/Koordination des Sicherheitsprozesses ab; zudem ist dort ein direktes Berichtsrecht an die Leitung vorgesehen. ISMS.1.A1 deckt die Gesamtverantwortung und die Festlegung von Zuständigkeiten durch die Leitung ab, was den Leitungsbezug der Rolle stützt. IND.1.A1 verlangt ebenfalls eine gesamtverantwortliche Person für Informationssicherheit im OT-Bereich. Keine der Kandidaten formuliert jedoch ausdrücklich, dass die Rolle des ISB in jeder Institution zwingend zu besetzen und unmittelbar der Institutionsleitung unterstellt sein muss.
- **Lücken:** Es fehlt die explizite Vorgabe, dass der ISB in jeder Institution unabhängig von Art und Größe verpflichtend zu besetzen ist, sowie die eindeutige unmittelbare Unterstellung unter die Institutionsleitung als Rollenbeschreibung. Außerdem ist die Benennung als generelle Governance-/Compliance-Anforderung nicht vollständig in der Tiefe abgebildet.

### GC.8.1.1.1.1 — Vorspracherecht des Informationssicherheitsbeauftragten
- **Confidence:** 0.91
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A12` [Standard] Management-Berichte zur Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `DER.3.2.A9` [Standard] Integration in den Informationssicherheitsprozess — _DER.3.2 Revisionen auf Basis des Leitfadens IS-Revision_
- **Begründung:** Die GS++-Anforderung fordert ausdrücklich das direkte Vorspracherecht des ISB bei der Institutionsleitung. ISMS.1.A4 deckt dies inhaltlich am nächsten ab, da die Institutionsleitung dem ISB die Möglichkeit einräumen MUSS, bei Bedarf direkt an sie selbst zu berichten. ISMS.1.A1 ergänzt die Pflicht der Leitung, sich regelmäßig über den Status der Informationssicherheit informieren zu lassen, und ISMS.1.A12 konkretisiert den regelmäßigen Bericht an die Leitung. DER.3.2.A9 ist ebenfalls relevant, weil dort der regelmäßige Bericht des ISB an die Institutionsleitung genannt wird. Eine explizite Verankerung eines jederzeitigen/uneingeschränkten direkten Vorspracherechts ist jedoch nicht vollständig enthalten.
- **Lücken:** Fehlt ist die explizite organisatorische Verankerung eines direkten Vorspracherechts als Recht des ISB gegenüber der Institutionsleitung. Die Kandidaten sprechen nur von der Möglichkeit bei Bedarf direkt zu berichten bzw. von regelmäßigen Berichten, nicht von einem formal zugesicherten Vorspracherecht ohne Zwischenschaltung anderer Stellen.

### GC.8.1.2 — Stellvertreterregelungen
- **Confidence:** 0.97
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A6` [Basis] Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** ISMS.1.A6 deckt den Kern der Anforderung ab, weil dort für alle wichtigen Funktionen der Informationssicherheitsorganisation wirksame Vertretungsregelungen gefordert werden. Damit ist die grundsätzliche Stellvertreterregelung im ISMS inhaltlich enthalten. Die Formulierung ist jedoch allgemeiner als GC.8.1.2 und verlangt nicht explizit Stellvertreterregelungen für alle relevanten Rollen und Zuständigkeiten im ISMS, sondern nur für wichtige Funktionen.
- **Lücken:** Nicht explizit abgedeckt ist die Forderung nach Stellvertreterregelungen für alle relevanten Rollen und Zuständigkeiten; ISMS.1.A6 spricht nur von wirksamen Vertretungsregelungen für wichtige Funktionen der Informationssicherheitsorganisation.

### GC.8.1.3 — Vermeidung von Interessenkonflikten
- **Confidence:** 0.84
- **Gemappte GS-Anforderungen:**
  - `OPS.1.1.1.A2` [Basis] Festlegung von Rollen und Berechtigungen für den IT-Betrieb — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `IND.3.2.A10` [Standard] Beobachtung und Kontrolle von OT-Fernwartungssitzungen — _IND.3.2 Fernwartung im industriellen Umfeld_
  - `IND.1.A1` [Basis] Einbindung in die Sicherheitsorganisation — _IND.1 Prozessleit- und Automatisierungstechnik_
  - `INF.13.A12` [Standard] Sichere Konfiguration der TGM-Systeme — _INF.13 Technisches Gebäudemanagement_
  - `INF.13.A14` [Standard] Berücksichtigung spezieller Rollen und Berechtigungen im TGM — _INF.13 Technisches Gebäudemanagement_
  - `OPS.1.1.2.A23` [Standard] Rollen- und Berechtigungskonzept für administrative Zugriffe — _OPS.1.1.2 Ordnungsgemäße IT-Administration_
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** Die Grundschutz++-Anforderung verlangt Maßnahmen zur Vermeidung von Interessenkonflikten bei der Festlegung von Rollen und Zuständigkeiten im ISMS, insbesondere die Trennung konkurrierender Rollen (z. B. ausführend vs. prüfend/freigebend) und organisatorische/verfahrenstechnische Maßnahmen wie Vier-Augen-Prinzip. Inhaltlich passen vor allem Anforderungen, die die Trennung von Administrations- und Betriebsaufgaben bzw. von Rollen und Berechtigungen fordern (OPS.1.1.1.A2, OPS.1.1.2.A23) sowie die explizite Vier-Augen-Regel (IND.3.2.A10, INF.13.A12). Anforderungen zur Benennung zuständiger Personen bzw. zur Verankerung von Rollen im ISMS (IND.1.A1, ORP.5.A4, INF.13.A14) decken nur den Aspekt Rollenfestlegung/Organisation ab, nicht aber die Vermeidung von Interessenkonflikten selbst.
- **Lücken:** Nicht vollständig abgedeckt ist der Kernaspekt einer expliziten Konfliktvermeidung bei der Rollenfestlegung im ISMS, also die allgemeine Regel, konkurrierende Rollen systematisch zu trennen oder andere Kompensationsmaßnahmen verbindlich festzulegen. Mehrere Kandidaten behandeln nur Rollen-/Berechtigungskonzepte oder die Benennung Verantwortlicher, aber ohne expliziten Bezug zu Interessenkonflikten, Prüffunktionen oder Freigabefunktionen im ISMS-Kontext.

### GC.8.1.4 — Festlegung einer Sicherheitsorganisation
- **Confidence:** 0.86
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.5.A8` [Standard] Regelmäßige Überprüfungen des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
  - `ORP.3.A8` [Standard] Messung und Auswertung des Lernerfolgs — _ORP.3 Sensibilisierung und Schulung zur Informationssicherheit_
  - `DER.3.2.A13` [Standard] Sichtung und Prüfung der Dokumente — _DER.3.2 Revisionen auf Basis des Leitfadens IS-Revision_
- **Begründung:** Die Anforderung GC.8.1.4 verlangt die Festlegung der Sicherheitsorganisation für das ISMS einschließlich Rollen, Zuständigkeiten und Gremien sowie die Verankerung relevanter Schnittstellen zu anderen Sicherheitsbereichen. ORP.5.A4 deckt die Festlegung von Zuständigen und geeigneten Organisationsstrukturen für das Compliance Management ab und enthält den Austausch mit dem ISB und anderen sicherheitsrelevanten Ansprechpartnern. ORP.5.A8 prüft explizit die Angemessenheit der Organisationsstruktur. ORP.3.A8 adressiert den regelmäßigen Austausch mit anderen sicherheitsrelevanten Ansprechpartnern, und DER.3.2.A13 verlangt, dass in Dokumenten wesentliche Aspekte erfasst und geeignete Rollen zugewiesen wurden. Zusammen nähern sich die Kandidaten dem Thema an, bilden aber die vollständige Sicherheitsorganisation des ISMS nicht ab.
- **Lücken:** Nicht abgedeckt sind die explizite Festlegung der Sicherheitsorganisation für das ISMS als Ganzes, die klare Benennung und Abbildung aller Rollen/Zuständigkeiten/Gremien über das gesamte ISMS hinweg sowie die geforderte vollständige Verankerung und Dokumentation der Schnittstellen zu weiteren Bereichen (z. B. Datenschutz, physische Sicherheit, Geheimschutz, Arbeitsschutz) in einer Organisationsdarstellung/ einem Organigramm.

### GC.8.1.5 — Sicherstellung der Qualifikation
- **Confidence:** 0.84
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A6` [Basis] Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `ORP.2.A15` [Basis] Qualifikation des Personals — _ORP.2 Personal_
  - `OPS.1.1.1.A16` [Standard] Schulung des Betriebspersonals — _OPS.1.1.1 Allgemeiner IT-Betrieb_
  - `CON.8.A1` [Standard] Definition von Rollen und Zuständigkeiten — _CON.8 Software-Entwicklung_
- **Begründung:** Die GS++-Anforderung verlangt, dass für jeden Rollen- und Verantwortungsträger die erforderlichen Anforderungen und Fähigkeiten festgelegt werden. Das wird inhaltlich am ehesten durch ISMS.1.A6 abgedeckt, da dort Rollen, Verantwortungen, Kompetenzen sowie qualifizierte Personen für das Informationssicherheitsmanagement definiert und zugewiesen werden müssen. ORP.2.A15 ergänzt dies um die Forderung, dass bei Stellenbesetzung die erforderlichen Qualifikationen und Fähigkeiten formuliert sein müssen und nur qualifizierte Mitarbeitende eingesetzt werden dürfen. OPS.1.1.1.A16 adressiert die Sicherstellung erforderlicher Fähigkeiten und Qualifikationen des Betriebspersonals durch Schulungsplanung. CON.8.A1 deckt die Festlegung von Rollen und Zuständigkeiten in einem konkreten Prozess ab. Gemeinsam berühren diese Anforderungen den Kern, jedoch nicht vollständig die explizite Vorgabe, für jeden Rollen- und Verantwortungsträger systematisch Anforderungen und Fähigkeiten festzulegen.
- **Lücken:** Nicht vollständig abgedeckt ist die explizite, allgemeingültige und rollenbezogene Festlegung der erforderlichen Anforderungen und Fähigkeiten für jeden Rollen- und Verantwortungsträger im Rahmen von Governance und Compliance. Die Kandidaten enthalten teils Organisations-, Rollen- oder Qualifikationsanforderungen, aber keine durchgängige Vorgabe zur vollständigen, individuellen Anforderungsdefinition für alle Rollen- und Verantwortungsträger.

### GC.8.1.6 — Ressourcen für den Informationssicherheitsbeauftragten
- **Confidence:** 0.91
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A4` [Basis] Benennung eines oder einer Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A6` [Basis] Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A5` [Basis] Vertragsgestaltung bei Bestellung eines oder einer externen Informationssicherheitsbeauftragten — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A1` [Basis] Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung — _ISMS.1 Sicherheitsmanagement_
  - `ISMS.1.A15` [Standard] Wirtschaftlicher Einsatz von Ressourcen für Informationssicherheit — _ISMS.1 Sicherheitsmanagement_
- **Begründung:** Die GS++-Anforderung verlangt, dem Informationssicherheitsbeauftragten (ISB) ausreichend Ressourcen zuzuweisen. Inhaltlich am nächsten kommen die Grundschutz-Anforderungen zur Benennung/Bestellung des ISB und zur Ausstattung mit angemessenen Ressourcen (ISMS.1.A4, ISMS.1.A6, ISMS.1.A1). ISMS.1.A5 deckt die Ressourcenthematik nur indirekt für externe ISB über den Vertrag ab. ISMS.1.A15 behandelt die Bereitstellung von Ressourcen für Informationssicherheit allgemein und die termingerechte Bereitstellung sowie Reserven, jedoch nicht spezifisch den ISB. Zusammen wird der Kern der Anforderung erfasst, aber nicht der explizite GS++-Aspekt, dass die Governance- und Compliance-Seite dem ISB konkret Ressourcen zuweisen muss, einschließlich ausreichender Zeit und der Vermeidung von Interessenkonflikten.
- **Lücken:** Nicht vollständig abgedeckt sind die explizite Zuweisung von Ressourcen durch Governance und Compliance an den ISB, die konkrete Sicherstellung ausreichender Zeit für ISB-Aufgaben sowie der Hinweis auf fehlende Interessenkonflikte bzw. Trennung zu anderen Aufgaben. Diese Aspekte werden in den Kandidaten nur teilweise oder gar nicht ausdrücklich genannt.

### GC.9.1 — Festlegung eines Verfahrens zum Kommunikationsmanagement
- **Confidence:** 0.83
- **Gemappte GS-Anforderungen:**
  - `DER.2.1.A4` [Basis] Benachrichtigung betroffener Stellen bei Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `DER.2.1.A5` [Basis] Behebung von Sicherheitsvorfällen — _DER.2.1 Behandlung von Sicherheitsvorfällen_
  - `NET.2.1.A1` [Basis] Festlegung einer Strategie für den Einsatz von WLANs — _NET.2.1 WLAN-Betrieb_
- **Begründung:** Die GS++-Anforderung fordert ein generelles Verfahren zum Kommunikationsmanagement für interne und externe ISMS-bezogene Kommunikation inklusive Festlegung von Eckpunkten (wer, wann, mit wem, wie), relevanter Behörden/Kontakte und Zuständigkeiten. DER.2.1.A4 deckt den Teil der externen bzw. internen Benachrichtigung bei Sicherheitsvorfällen inklusive Behörden und betroffener Stellen ab. DER.2.1.A5 verlangt eine Liste relevanter interner und externer Fachstellen sowie sichere Kommunikationsverfahren mit diesen Stellen. NET.2.1.A1 enthält zudem die Festlegung von Zuständigkeiten und Schnittstellen sowie den Austausch von Informationen zwischen Zuständigen. Zusammen ergeben die Kandidaten jedoch nur Teilaspekte eines Kommunikationsmanagement-Verfahrens, nicht das umfassende Governance-Verfahren selbst.
- **Lücken:** Es fehlt die explizite, allgemeine Verankerung eines übergreifenden Kommunikationsmanagement-Prozesses für das ISMS mit klaren Regeln für alle relevanten Kommunikationsarten (intern/extern) außerhalb von Incident- und WLAN-Kontexten. Auch die systematische Festlegung von Kommunikationsanlässen, -wegen und -formalitäten (wer/wann/mit wem/wie) als generelles Verfahren ist nicht vollständig abgedeckt.

### GC.9.1.1 — Externer Austausch zur Informationssicherheit
- **Confidence:** 0.83
- **Gemappte GS-Anforderungen:**
  - `ORP.5.A4` [Standard] Konzeption und Organisation des Compliance Managements — _ORP.5 Compliance Management (Anforderungsmanagement)_
- **Begründung:** ORP.5.A4 ist der einzige Kandidat mit inhaltlicher Nähe, da dort ausdrücklich ein regelmäßiger Austausch zwischen Compliance-Beauftragten und Informationssicherheitsbeauftragten gefordert wird. Das deckt jedoch nur den internen Abstimmungsaspekt ab, nicht den geforderten externen Austausch zur Informationssicherheit. Die übrigen Kandidaten behandeln andere Themen (Outsourcing, Fernwartung, Austausch von Informationen, technische Schnittstellen) und passen nicht inhaltlich.
- **Lücken:** Es fehlt die explizite Anforderung an einen externen Austausch bzw. eine externe Vernetzung zur Wahrnehmung anderer Perspektiven (z. B. mit Branchenverbänden, Fachforen oder ähnlichen Einrichtungen).

### GC.9.1.3 — Dokumentenlenkung
- **Confidence:** 0.89
- **Gemappte GS-Anforderungen:**
  - `ISMS.1.A13` [Standard] Dokumentation des Sicherheitsprozesses — _ISMS.1 Sicherheitsmanagement_
  - `OPS.1.2.2.A9` [Basis] Auswahl geeigneter Datenformate für die Archivierung von Dokumenten — _OPS.1.2.2 Archivierung_
  - `CON.9.A5` [Standard] Beseitigung von Restinformationen vor Weitergabe — _CON.9 Informationsaustausch_
  - `OPS.1.2.5.A7` [Standard] Dokumentation bei der Fernwartung — _OPS.1.2.5 Fernwartung_
  - `SYS.1.8.A17` [Standard] Dokumentation der Systemeinstellungen von Speichersystemen — _SYS.1.8 Speicherlösungen_
- **Begründung:** Die GS++-Anforderung fordert ein durchgängiges Verfahren zur Dokumentenlenkung über den gesamten Lebenszyklus inklusive Erstellung/Übernahme, Metadaten, Versionierung, Veröffentlichung, geschützter Ablage, Archivierung und Rücknahme. ISMS.1.A13 deckt die geregelte Erstellung, Archivierung, Aktualität und die Verfügbarkeit aktueller sowie archivierter Versionen von ISMS-Dokumenten ab. OPS.1.2.2.A9 adressiert die Archivierung und langfristige Reproduzierbarkeit, also den Archivierungsaspekt. CON.9.A5 deckt die Prüfung und Bereinigung vor Weitergabe bzw. Veröffentlichung von Dokumenten ab. OPS.1.2.5.A7 und SYS.1.8.A17 enthalten Anforderungen an Dokumentation, geschützte Ablage und Aktualität, jedoch jeweils nur für spezifische Themenbereiche. Zusammen ergeben sie eine inhaltliche Teilabdeckung der Dokumentenlenkung, aber kein vollständiges Lifecycle-Verfahren mit allen geforderten Metadaten, Rücknahme und einheitlichen Formaten.
- **Lücken:** Nicht abgedeckt sind insbesondere ein explizit festgelegtes Dokumentenlenkungsverfahren für das gesamte ISMS, die verbindliche Erfassung von Metadaten wie Titel, Autor, Dokumenteneigentümer, Sicherheitsklassifikation und Erstelldatum, die formale Änderungssteuerung/Versionierung als durchgängiger Prozess, die einheitliche Veröffentlichung sowie die ausdrückliche Rücknahme von Dokumenten.

## Keine Abdeckung (1)

### GC.3.2 — Analyse der internen interessierten Parteien
- **Confidence:** 0.94
- **Begründung:** Keine der Kandidatenanforderungen fordert ein Verfahren zum Ermitteln aller internen interessierten Parteien und ihrer Bedürfnisse und Erwartungen an das Informationssicherheitsmanagement. Die genannten Anforderungen behandeln Compliance-Management, rechtliche Rahmenbedingungen, Incident-Kommunikation, Admin-Berechtigungen, Outsourcing oder technische Sicherheitsmaßnahmen, aber nicht die systematische Identifikation interner Stakeholder und deren Erwartungen.
- **Lücken:** Es fehlt eine explizite Anforderung zur Ermittlung interner interessierter Parteien (z. B. Geschäftsführung, Mitarbeitende, Führungskräfte, Betriebs-/Personalrat) sowie zur Erfassung ihrer Bedürfnisse und Erwartungen an das ISMS.
