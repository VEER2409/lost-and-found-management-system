CREATE DATABASE IF NOT EXISTS lost_and_found;

USE lost_and_found;

-- Main table for every found item/case
CREATE TABLE IF NOT EXISTS found_items (
    case_id VARCHAR(10) PRIMARY KEY,

    category ENUM(
        'Electronics',
        'ID / Documents',
        'Jewelry',
        'Bags & Accessories',
        'Clothing',
        'Books & Stationery',
        'Keys',
        'Office Equipment',
        'Personal Items',
        'Other'
    ) NOT NULL,

    item_name VARCHAR(100) NOT NULL,
    brand VARCHAR(50),
    model VARCHAR(100),
    description TEXT NOT NULL,

    found_location VARCHAR(150) NOT NULL,
    found_date DATE NOT NULL,

    finder_name VARCHAR(100) NOT NULL,
    finder_employee_id VARCHAR(20) NOT NULL,

    storage_location VARCHAR(100),

    status ENUM(
        'Awaiting Claim',
        'Claim Under Verification',
        'Returned',
        'Unclaimed',
        'Donated',
        'Disposed'
    ) NOT NULL DEFAULT 'Awaiting Claim'
);


-- Stores claims made against found items
CREATE TABLE IF NOT EXISTS claims (
    claim_id VARCHAR(10) PRIMARY KEY,

    case_id VARCHAR(10) NOT NULL,

    claimant_name VARCHAR(100) NOT NULL,
    claimant_employee_id VARCHAR(20) NOT NULL,

    claim_date DATE NOT NULL,

    claim_description TEXT NOT NULL,

    claim_status ENUM(
        'Pending',
        'Approved',
        'Rejected'
    ) NOT NULL DEFAULT 'Pending',

    verified_by_employee_id VARCHAR(20),

    CONSTRAINT fk_claim_case
        FOREIGN KEY (case_id)
        REFERENCES found_items(case_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);