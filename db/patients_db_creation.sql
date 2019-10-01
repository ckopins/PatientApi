CREATE DATABASE patients_db
    WITH 
    OWNER = (SELECT current_user)
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE public."Patient"
(
    created_by character varying(100) COLLATE pg_catalog."default",
    created_date date NOT NULL,
    enterprise_id character varying(50) COLLATE pg_catalog."default",
    id integer NOT NULL DEFAULT nextval('"Patient_id_seq"'::regclass),
    last_modified_date date NOT NULL,
    last_modified_by character varying COLLATE pg_catalog."default",
    CONSTRAINT "Patient_pkey" PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Patient"
    OWNER to (SELECT current_user);

CREATE TABLE public."PatientAddress"
(
    id integer NOT NULL DEFAULT nextval('"PatientAddress_id_seq"'::regclass),
    created_by character varying(100) COLLATE pg_catalog."default",
    created_date date NOT NULL,
    last_modified_by character varying(100) COLLATE pg_catalog."default",
    last_modified_date date NOT NULL,
    address_line_1 character varying(100) COLLATE pg_catalog."default",
    address_line_2 character varying(100) COLLATE pg_catalog."default",
    city character varying(50) COLLATE pg_catalog."default",
    state character varying(50) COLLATE pg_catalog."default",
    zip_code character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "PatientAddress_pkey" PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."PatientAddress"
    OWNER to (SELECT current_user);

CREATE TABLE public."PatientMemberRecord"
(
    id integer NOT NULL DEFAULT nextval('"PatientMemberRecord_id_seq"'::regclass),
    created_by character varying COLLATE pg_catalog."default",
    created_date date NOT NULL,
    last_modified_by character varying COLLATE pg_catalog."default",
    last_modified_date date NOT NULL,
    source character varying(256) COLLATE pg_catalog."default",
    medical_record_number character varying(128) COLLATE pg_catalog."default",
    first_name character varying(64) COLLATE pg_catalog."default",
    last_name character varying(64) COLLATE pg_catalog."default",
    social_security_number character varying(11) COLLATE pg_catalog."default",
    patient_id integer NOT NULL,
    patient_address_id integer NOT NULL,
    CONSTRAINT "PatientMemberRecord_pkey" PRIMARY KEY (id),
    CONSTRAINT "FK_PatientMemberRecord_Patient" FOREIGN KEY (patient_id)
        REFERENCES public."Patient" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_PatientMemberRecord_PatientAddress" FOREIGN KEY (patient_address_id)
        REFERENCES public."PatientAddress" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."PatientMemberRecord"
    OWNER to (SELECT current_user);

CREATE INDEX "fki_FK_PatientMemberRecord_Patient"
    ON public."PatientMemberRecord" USING btree
    (patient_id)
    TABLESPACE pg_default;

CREATE INDEX "fki_FK_PatientMemberRecord_PatientAddress"
    ON public."PatientMemberRecord" USING btree
    (patient_address_id)
    TABLESPACE pg_default;

CREATE TABLE public."Log"
(
    id integer NOT NULL DEFAULT nextval('"Log_id_seq"'::regclass),
    logger character varying(1024) COLLATE pg_catalog."default",
    level character varying(32) COLLATE pg_catalog."default",
    trace character varying(1024) COLLATE pg_catalog."default",
    msg character varying(1024) COLLATE pg_catalog."default",
    created_by character varying(64) COLLATE pg_catalog."default",
    created_date date NOT NULL,
    last_modified_by character varying(64) COLLATE pg_catalog."default",
    last_modified_date date NOT NULL,
    CONSTRAINT "Log_pkey" PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Log"
    OWNER to (SELECT current_user);