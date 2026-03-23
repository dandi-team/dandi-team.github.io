import os
import pathlib
import nox
import sys

# for some reason necessary to correctly import conf from cwd
sys.path.insert(0, str(pathlib.Path(__file__).parent.absolute()))
import conf


## Sphinx related options

# Sphinx output and source directories
BUILD_DIR = "_build"
OUTPUT_DIR = pathlib.Path(BUILD_DIR, "html")
SOURCE_DIR = pathlib.Path(".")

# Location of the translation templates
TRANSLATION_LOCALES_DIR = pathlib.Path("locales")

# Sphinx build commands
SPHINX_BUILD = "sphinx-build"
SPHINX_AUTO_BUILD = "sphinx-autobuild"

# Sphinx parameters used to build the guide
BUILD_PARAMETERS = ["-b", "html"]

# Sphinx-autobuild ignore and include parameters
AUTOBUILD_IGNORE = [
    "_build",
    ".nox",
    "build_assets",
    "tmp",
]
AUTOBUILD_INCLUDE = [pathlib.Path("_static")]

## Localization options (translations)
# List of languages that should be built when releasing the guide (docs session)
LANGUAGES = conf.languages


@nox.session
def docs(session):
    """Build the website."""
    session.install("-e", ".")
    session.run(
        SPHINX_BUILD, *BUILD_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs
    )
    # When building the guide, also build the translations in LANGUAGES
    session.notify("build-languages", session.posargs)


@nox.session(name="build-language")
def build_language(session):
    """
    Build the guide for a specific language translation

    For example: nox -s build-language -- fr.
    """
    if session.posargs and (lang := session.posargs.pop(0)):
        if lang in LANGUAGES:
            session.install("-e", ".")
            session.log(f"Building [{lang}] guide")
            session.run(
                SPHINX_BUILD,
                *BUILD_PARAMETERS,
                "-D",
                f"language={lang}",
                ".",
                OUTPUT_DIR / lang,
                *session.posargs,
            )
        else:
            session.error(f"Language {lang} is not in LANGUAGES list.")
    else:
        session.error(
            "Please provide a language using:\n\n      "
            "nox -s build-language -- LANG\n\n     "
            f" where LANG is one of: {LANGUAGES}"
        )


@nox.session(name="build-release-languages")
def build_release_languages(session):
    """
    Build the translations of the guide for the languages in RELEASE_LANGUAGES.
    """
    session.install("-e", ".")
    for lang in LANGUAGES:
        session.log(f"Building [{lang}] guide")
        session.run(
            SPHINX_BUILD,
            *BUILD_PARAMETERS,
            "-D",
            f"language={lang}",
            ".",
            OUTPUT_DIR / lang,
            *session.posargs,
        )
        if lang == "en":
            out_dir = OUTPUT_DIR
        else:
            out_dir = OUTPUT_DIR / lang
        session.run(
            SPHINX_BUILD,
            *BUILD_PARAMETERS,
            "-D",
            f"language={lang}",
            ".",
            out_dir,
            *session.posargs,
            env={"SPHINX_LANG": lang},
        )
    session.log(f"Translations built for {LANGUAGES}")


@nox.session(name="build-all-languages")
def build_all_languages(session):
    """
    Build the translations of the guide for the languages in LANGUAGES.
    """
    if not LANGUAGES:
        session.warn("No languages defined in LANGUAGES")
        return
    session.install("-e", ".")
    for lang in LANGUAGES:
        session.log(f"Building [{lang}] guide")
        session.run(
            SPHINX_BUILD,
            *BUILD_PARAMETERS,
            "-D",
            f"language={lang}",
            ".",
            OUTPUT_DIR / lang,
            *session.posargs,
        )
    session.log(f"Translations built for {LANGUAGES}")

    BUILD_LANGUAGES = LANGUAGES
    # only build languages that have a locale folder
    BUILD_LANGUAGES = [
        lang for lang in BUILD_LANGUAGES if (TRANSLATION_LOCALES_DIR / lang).exists()
    ]
    session.notify("build-languages", [BUILD_LANGUAGES, *session.posargs])
