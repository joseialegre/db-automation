SELECT a.*
FROM CLI_ClientePersona a WITH (NOLOCK)
LEFT JOIN CLI_PERSONASFISICAS b WITH (NOLOCK)
ON a.NumeroPersona = b.NumeroPersonaFisica
LEFT JOIN CLI_PERSONASJURIDICAS c WITH (NOLOCK)
ON a.NumeroPersona = c.NumeroPersonaJuridica
WHERE b.NumeroPersonaFisica IS NULL AND c.NumeroPersonaJuridica IS NULL