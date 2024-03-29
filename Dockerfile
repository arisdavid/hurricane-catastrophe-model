FROM python:3.6

RUN mkdir -p /usr/oasis

WORKDIR /usr/oasis

COPY . /usr/oasis

RUN pip install --no-cache-dir -r requirements.txt

# Run pytest with coverage. Ideally this should be done with a CI/CD
RUN python -m pytest --cov=src/tests

# Add project path to PATH
ENV PATH /usr/oasis:$PATH

# For running in a windows host machine
RUN apt-get update
RUN apt-get install dos2unix
RUN dos2unix gethurricaneloss


