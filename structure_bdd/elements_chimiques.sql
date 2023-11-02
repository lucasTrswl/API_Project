-- Table: public.elements_chimiques

-- DROP TABLE IF EXISTS public.elements_chimiques;

CREATE TABLE IF NOT EXISTS public.elements_chimiques
(
    code_element character varying(5) COLLATE pg_catalog."default" NOT NULL,
    un character varying(20) COLLATE pg_catalog."default" NOT NULL,
    libelle_element character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT elements_chimiques_pkey PRIMARY KEY (code_element),
    CONSTRAINT un FOREIGN KEY (un)
        REFERENCES public.unite (un) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.elements_chimiques
    OWNER to postgres;