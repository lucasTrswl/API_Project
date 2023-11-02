-- Table: public.unite

-- DROP TABLE IF EXISTS public.unite;

CREATE TABLE IF NOT EXISTS public.unite
(
    un character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT unite_pkey PRIMARY KEY (un)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.unite
    OWNER to postgres;