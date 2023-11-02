-- Table: public.date

-- DROP TABLE IF EXISTS public.date;

CREATE TABLE IF NOT EXISTS public.date
(
    date date NOT NULL,
    CONSTRAINT date_pkey PRIMARY KEY (date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.date
    OWNER to postgres;