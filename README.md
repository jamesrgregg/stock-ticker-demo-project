# bolt-generated-python-stock-ticker-project
To use this tool you need to have API keys to [FMP](https://site.financialmodelingprep.com/), and a Groq API key.

Copy .env-example to .env and update with your keys.


## Demo 
We want to demo a developer flow using a modern AI solution such as Bolt.diy where the AI bot can look at a repo, inventory the code and create a workflow that does the following:
 - inventory
 - source code checkout
 - set up a build environment
 - build
 - test
 - scan
 - create an SBOM
 - create the attestation for SLSA Level3
 - push artifacts
 - package the application (containerize the software)
 - release the package as a versioned artifact