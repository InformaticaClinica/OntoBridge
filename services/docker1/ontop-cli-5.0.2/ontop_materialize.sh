# Change the directory where this script is located
cd "$(dirname "$0")"

# ontop materialize command
ontop materialize -m /app/data/full.ttl -p /app/data/ontobridge.properties -o /app/data/rdf_output.ttl -f turtle

