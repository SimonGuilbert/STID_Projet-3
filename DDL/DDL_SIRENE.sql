

CREATE TABLE SIRENE (
SIREN TEXT, -- code entreprise
NIC TEXT, -- code etablissement
L1_normalisee TEXT, -- nom etablissement
DEPET TEXT, -- departement
COMET TEXT, -- commune
APET700 TEXT -- code naf niveau 5
);

ALTER TABLE SIRENE ADD COLUMN CODE_INSEE TEXT;
UPDATE SIRENE SET CODE_INSEE = DEPET || COMET WHERE DEPET IS NOT NULL AND COMET IS NOT NULL;
CREATE INDEX code_insee_idx ON SIRENE(CODE_INSEE);
CREATE INDEX departement_idx ON SIRENE(departement);

