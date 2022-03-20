#!/bin/bash
export DATABASE_URL="postgresql://postgres:1701@localhost:5432/car"
export DATABASE_TEST_URL="postgresql://postgres:1701@localhost:5432/car_test"
echo "setup.sh script executed successfully!"