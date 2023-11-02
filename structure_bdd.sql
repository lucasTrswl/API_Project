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