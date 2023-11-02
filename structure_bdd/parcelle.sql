-- Table: public.parcelle

-- DROP TABLE IF EXISTS public.parcelle;

CREATE TABLE IF NOT EXISTS public.parcelle
(
    no_parcelle smallint NOT NULL,
    surface numeric(50,0) NOT NULL,
    nom_parcelle character varying(20) COLLATE pg_catalog."default" NOT NULL,
    coordonnees character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT parcelle_pkey PRIMARY KEY (no_parcelle)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.parcelle
    OWNER to postgres;