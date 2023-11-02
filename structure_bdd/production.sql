-- Table: public.production

-- DROP TABLE IF EXISTS public.production;

CREATE TABLE IF NOT EXISTS public.production
(
    code_production smallint NOT NULL,
    un character varying(20) COLLATE pg_catalog."default" NOT NULL,
    nom_production character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT production_pkey PRIMARY KEY (code_production),
    CONSTRAINT un FOREIGN KEY (un)
        REFERENCES public.unite (un) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.production
    OWNER to postgres;