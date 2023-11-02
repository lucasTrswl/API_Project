-- Table: public.epandre

-- DROP TABLE IF EXISTS public.epandre;

CREATE TABLE IF NOT EXISTS public.epandre
(
    id_engrais uuid NOT NULL,
    no_parcelle smallint NOT NULL,
    date date NOT NULL,
    qte_epandue numeric(50,0) NOT NULL,
    CONSTRAINT epandre_pkey PRIMARY KEY (id_engrais),
    CONSTRAINT date FOREIGN KEY (date)
        REFERENCES public.date (date) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT id_engrais FOREIGN KEY (id_engrais)
        REFERENCES public.engrais (id_engrais) MATCH SIMPLE
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

ALTER TABLE IF EXISTS public.epandre
    OWNER to postgres;