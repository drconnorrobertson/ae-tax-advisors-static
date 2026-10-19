# Booking measurement contract

`assets/booking-events.js` emits `ae_booking_cta_click`, `ae_calendar_open` and
`ae_calendar_view` into `window.dataLayer` and the existing `ae:marketing-event`
DOM integration channel. It transmits no data to a new analytics provider and
does not load a remote tag. Parameters contain sanitized page and destination
paths/hostnames, never query strings or form fields.

These events measure intent and calendar exposure, not appointments. Completed
bookings must come from the CRM's confirmed appointment record. Do not infer
completion from an iframe load or a message from a frame. Attribute qualified
calls in the CRM, keeping appointment/contact identifiers out of public pages.

No GA4/GTM destination is configured in this change. Connect the approved AE
measurement destination and verify its receipt before claiming production
analytics collection. Do not substitute another company's measurement ID.

Validation: `node scripts/test-booking-events.cjs`.
