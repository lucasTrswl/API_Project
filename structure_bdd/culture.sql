-- Table: public.culture

-- DROP TABLE IF EXISTS public.culture;

CREATE TABLE IF NOT EXISTS public.culture
(
    identifiant_culture smallint NOT NULL,
    no_parcelle smallint NOT NULL,
    code_production smallint NOT NULL,
    date_debut date NOT NULL,
    date_fin date NOT NULL,
    qte_recoltee numeric(20,0) NOT NULL,
    CONSTRAINT culture_pkey PRIMARY KEY (identifiant_culture),
    CONSTRAINT code_production FOREIGN KEY (code_production)
        REFERENCES public.production (code_production) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT no_parcelle FOREIGN KEY (no_parcelle)
        REFERENCES public.parcelle (no_parcelle) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.culture
    OWNER to postgres;