-- Table: public.engrais

-- DROP TABLE IF EXISTS public.engrais;

CREATE TABLE IF NOT EXISTS public.engrais
(
    id_engrais uuid NOT NULL,
    un character varying(20) COLLATE pg_catalog."default" NOT NULL,
    nom_engrais character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT engrais_pkey PRIMARY KEY (id_engrais),
    CONSTRAINT un FOREIGN KEY (un)
        REFERENCES public.unite (un) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.engrais
    OWNER to postgres;