# coding=utf-8

TERRITORIALE = 'T'
LOCALE = 'L'
PROVINCIALE = 'P'
REGIONALE = 'R'
NAZIONALE = 'N'
ESTENSIONE = (
    (TERRITORIALE, 'Unità Territoriale'),
    (LOCALE, 'Comitato Locale'),
    (PROVINCIALE, 'Comitato Provinciale'),
    (REGIONALE, 'Comitato Regionale'),
    (NAZIONALE, 'Comitato Nazioanle')
)

# Ad uso di comparazione
ESTENSIONE_MINORE = {
    TERRITORIALE: [],
    LOCALE: [TERRITORIALE],
    PROVINCIALE: [LOCALE, TERRITORIALE],
    REGIONALE: [PROVINCIALE, LOCALE, TERRITORIALE],
    NAZIONALE: [REGIONALE, PROVINCIALE, LOCALE, TERRITORIALE]
}