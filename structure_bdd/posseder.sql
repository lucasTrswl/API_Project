-- Table: public.posseder

-- DROP TABLE IF EXISTS public.posseder;

CREATE TABLE IF NOT EXISTS public.posseder
(
    id_engrais uuid NOT NULL,
    code_element character varying(5) COLLATE pg_catalog."default" NOT NULL,
    valeur character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT posseder_pkey PRIMARY KEY (id_engrais),
    CONSTRAINT code_element FOREIGN KEY (code_element)
        REFERENCES public.elements_chimiques (code_element) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT id_engrais FOREIGN KEY (id_engrais)
        REFERENCES public.engrais (id_engrais) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.posseder
    OWNER to postgres;