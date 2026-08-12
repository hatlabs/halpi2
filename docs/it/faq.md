---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# Domande frequenti

## Perché l’HALPI2 si riavvia dopo essere stato spento?

Il dispositivo ha il riavvio automatico abilitato: con `auto_restart` impostato su `true`, il controller riavvia il sistema circa 5 secondi dopo uno spegnimento da software se l’alimentazione di ingresso è collegata. Le unità prodotte prima dell’inizio del 2026 venivano fornite così; le unità attuali vengono fornite con la funzione disabilitata. La si può disattivare con `halpi config set auto_restart false` — oppure mantenerla, poiché garantisce che un sistema non presidiato non resti spento dopo un comando di spegnimento accidentale. Con la funzione abilitata, per spegnere definitivamente togliere l’alimentazione di ingresso. Vedere [Spegnimento](user-guide/operation.md#spegnimento).

## Come si spegne l’HALPI2?

Togliere l’alimentazione di ingresso. Il sistema rileva la mancanza di alimentazione e si spegne in modo controllato alimentandosi dai supercondensatori — è questo il modo previsto per spegnerlo. Vedere [Spegnimento](user-guide/operation.md#spegnimento).

## Occorre fare qualcosa quando manca l’alimentazione?

No. I disturbi brevi vengono coperti dai supercondensatori, le interruzioni più lunghe attivano uno spegnimento sicuro automatico e il sistema si riavvia da solo quando l’alimentazione ritorna. Vedere [In caso di mancanza di alimentazione](user-guide/operation.md#in-caso-di-mancanza-di-alimentazione).

## Quanto dura l’alimentazione di riserva?

I supercondensatori forniscono 30–60 secondi, a seconda del carico del sistema. È un tempo sufficiente, con margine, per uno spegnimento sicuro, ma l’HALPI2 non è un UPS — non continua a funzionare durante interruzioni prolungate. Vedere [Alimentazione in dettaglio](technical-reference/power-supply.md).

## L’HALPI2 può restare acceso 24 ore su 24?

Sì. L’HALPI2 è progettato per il funzionamento continuo non presidiato e la sua gestione dell’alimentazione lo presuppone: il sistema si riprende dalle mancanze di alimentazione e dai blocchi del sistema operativo senza intervento dell’utente.

## Che cosa significa quando i LED restano gialli?

Una barra gialla indica che il sistema è in esecuzione ma il demone HALPI non si è connesso — una condizione normale per un breve periodo durante l’avvio. Una barra gialla persistente indica che il sistema operativo non si avvia o che il demone non è installato. Vedere [Risoluzione dei problemi](user-guide/troubleshooting.md#i-led-restano-gialli).
