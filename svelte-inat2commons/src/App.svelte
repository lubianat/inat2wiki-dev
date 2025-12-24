<script>
  import { onMount, onDestroy, tick } from "svelte";

  const supportedLanguages = ["en", "es", "pt"];

  const translations = {
    es: {
      "A tool to connect iNaturalist and Wikimedia projects.":
        "Una herramienta para conectar iNaturalist con los proyectos de Wikimedia.",
      "Toggle navigation": "Alternar navegación",
      Language: "Idioma",
      Home: "Inicio",
      "Parse observation": "Analizar observación",
      "Code and feedback in the": "Código y comentarios en el",
      "GitHub repository": "repositorio en GitHub",
      "Privacy & Cookies": "Privacidad y cookies",
      "iNat2Wiki Logo": "Logo de iNat2Wiki",
      "We set one first‑party cookie called": "Establecemos una cookie propia llamada",
      "to remember your language choice. It expires when you close your browser and is never shared. No tracking, no analytics.":
        "para recordar tu elección de idioma. Expira al cerrar el navegador y nunca se comparte. Sin rastreo, sin análisis.",
      Privacy: "Privacidad",
      iNat2Wiki: "iNat2Wiki",
      "iNat2Wiki is an interface between iNaturalist and Wikimedia projects.":
        "iNat2Wiki es una interfaz entre iNaturalist y los proyectos de Wikimedia.",
      "This is a slow rewrite of the original tool, with a single goal of adding pictures of particular observations to commons via":
        "Esta es una reescritura lenta de la herramienta original, con el único objetivo de añadir imágenes de observaciones particulares al Commons a través de",
      "User observations": "Observaciones del usuario",
      "Enter the observation id": "Introduce el ID de la observación",
      Submit: "Enviar",
      "See an example": "Ver un ejemplo",
      Observation: "Observación",
      "Wikidata page": "Página de Wikidata",
      "Observation on iNaturalist": "Observación en iNaturalist",
      Image: "Imagen",
      License: "Licencia",
      "Link to Commons": "Enlace a Commons",
      "Upload to Commons": "Subir a Commons",
      "License not supported": "Licencia no compatible",
      "User list": "Lista de usuarios",
      "Project list": "Lista de proyectos",
      "Portuguese Wikipedia Stub": "Esbozo de Wikipedia en portugués",
      About: "Acerca de",
      "This tool is being rebuilt! Check out the new version at":
        "¡Esta herramienta está siendo reconstruida! Consulta la nueva versión en",
      "and leave feedback or feature requests on the":
        "y deja comentarios o solicitudes de funciones en el",
      "Enter the iNaturalist username below:":
        "Ingrese el nombre de usuario de iNaturalist a continuación:",
      "Enter the iNaturalist project name below:":
        "Ingrese el nombre del proyecto de iNaturalist a continuación:",
      "Enter the taxon QID or scientific name below:":
        "Ingrese el QID del taxón o el nombre científico a continuación:",
      "Enter QID or scientific name": "Ingrese QID o nombre científico",
      "Username:": "Nombre de usuario:",
      "Project name:": "Nombre del proyecto:",
      "Limit of observations (defaults to 200):":
        "Límite de observaciones (predeterminado 200):",
      "Wikipedia langcodes (defaults to 'en,pt'):":
        "Códigos de idioma de Wikipedia (predeterminado 'en,pt'):",
      "Research grade only?": "¿Solo grado de investigación?",
      "Open license only?": "¿Solo licencia abierta?",
      Go: "Ir",
      "Loading observations...": "Cargando observaciones...",
      "Taxa seen by {name}": "Taxones vistos por {name}",
      "Taxa observed in the scope of the project \"{project}\"":
        "Taxones observados en el ámbito del proyecto \"{project}\"",
      "Next {limit}": "Próximos {limit}",
      "Parsing up to {limit} most recent uploads (page {page}).":
        "Analizando hasta {limit} cargas más recientes (página {page}).",
      Group: "Grupo",
      "Taxon Name": "Nombre del taxón",
      "Number of observations": "Número de observaciones",
      "Observations by {name}": "Observaciones de {name}",
      "Wikidata ID": "ID de Wikidata",
      "Wikipages missing": "Páginas de Wikipedia ausentes",
      "create stub": "crear esbozo",
      "Scientific name not found.": "Nombre científico no encontrado.",
      "Generating stub...": "Generando esbozo...",
      "Stub for the Portuguese Wikipedia": "Esbozo para la Wikipedia en portugués",
      "Stub for the Spanish Wikipedia": "Esbozo para la Wikipedia en español",
      "Stub for the English Wikipedia": "Esbozo para la Wikipedia en inglés",
      "Stub for the French Wikipedia": "Esbozo para la Wikipedia en francés",
      "Portuguese Wikipedia page:": "Página de Wikipedia en portugués:",
      "Spanish Wikipedia page:": "Página de Wikipedia en español:",
      "English Wikipedia page:": "Página de Wikipedia en inglés:",
      "French Wikipedia page:": "Página de Wikipedia en francés:",
      "Powered by": "Impulsado por",
      "Code fully open source and open to contributions at the":
        "Código totalmente abierto y con contribuciones en el",
      "Special thanks to Andra Waagmeester and Dario Taraborelli for the guidance in the Open Biodiversity Knowledge / iNaturalist / eBird / Wiki / digital naturalism world.":
        "Agradecimientos especiales a Andra Waagmeester y Dario Taraborelli por la orientación en el mundo de Open Biodiversity Knowledge / iNaturalist / eBird / Wiki / naturalismo digital.",
      "See also Andra's": "Véase también el",
      "for more cool stuff like this": "para más cosas geniales como esta",
      Contributors: "Colaboradores",
      "Your name will go here! :)": "¡Tu nombre irá aquí! :)",
      "iNat2Wiki is a Flask App developed by Tiago Lubiana":
        "iNat2Wiki es una aplicación Flask desarrollada por Tiago Lubiana",
      "inspired by the": "inspirada por el",
      "Taxa observed in the scope of the project":
        "Taxones observados en el ámbito del proyecto",
      "An unexpected error (500) has occurred": "Ha ocurrido un error inesperado (500)",
      "File Not Found (404)": "Archivo no encontrado (404)",
      Back: "Volver",
      "Something wrong happened! Maybe the user with id '{id}' does not exist?":
        "¡Algo salió mal! ¿Quizás el usuario con id '{id}' no existe?",
      "Something wrong happened! Maybe the project with id '{id}' does not exist?":
        "¡Algo salió mal! ¿Quizás el proyecto con id '{id}' no existe?",
      "Failed to generate stub.": "No se pudo generar el esbozo.",
      Upload: "Subir"
    },
    pt: {
      "A tool to connect iNaturalist and Wikimedia projects.":
        "iNat2Wiki é uma interface entre o iNaturalist e os projetos da Wikimedia.",
      "Toggle navigation": "Alternar navegação",
      Language: "Idioma",
      "Parse observation": "Processar observação",
      "License not supported": "Licença não suportada",
      "Observation Details": "Detalhes da observação",
      "Page not found": "Página não encontrada",
      "An internal error occurred": "Ocorreu um erro interno",
      iNat2Wiki: "iNat2Wiki",
      "iNat2Wiki is an interface between iNaturalist and Wikimedia projects.":
        "iNat2Wiki é uma interface entre o iNaturalist e os projetos da Wikimedia.",
      "This is a slow rewrite of the original tool, with a single goal of adding pictures of particular observations to commons via":
        "Esta é uma reescrita lenta da ferramenta original, com o único objetivo de adicionar fotos de observações específicas ao Commons via",
      "User observations": "Observações do usuário",
      "Enter the observation id": "Entre o ID da observação",
      Submit: "Enviar",
      "See an example": "Veja um exemplo",
      Observation: "Observação",
      "Wikidata page": "Página da Wikidata",
      "Observation on iNaturalist": "Observação no iNaturalist",
      Image: "Imagem",
      License: "Licença",
      "Link to Commons": "Link para o Commons",
      "Upload to Commons": "Enviar para o Commons",
      "Privacy & Cookies": "Privacidade & Cookies",
      "We set one first‑party cookie called": "Nós provemos apenas um cookie chamado",
      "iNat2Wiki Logo": "Logo do iNat2Wiki",
      "to remember your language choice. It expires when you close your browser and is never shared. No tracking, no analytics.":
        "para lembrar sua escolha de linguagem. Ele espira ao fechar o browser e nunca é compartilhado. Sem rastreamento, sem analytics.",
      Privacy: "Privacidade",
      "GitHub repository": "repositório no GitHub",
      "Code and feedback in the": "Código e comentários no",
      "User list": "Lista de usuários",
      "Project list": "Lista de projetos",
      "Portuguese Wikipedia Stub": "Esboço da Wikipédia em português",
      About: "Sobre",
      "This tool is being rebuilt! Check out the new version at":
        "Esta ferramenta está sendo reconstruída! Confira a nova versão em",
      "and leave feedback or feature requests on the":
        "e deixe comentários ou solicitações de recursos no",
      "Enter the iNaturalist username below:":
        "Digite o nome de usuário do iNaturalist abaixo:",
      "Enter the iNaturalist project name below:":
        "Digite o nome do projeto do iNaturalist abaixo:",
      "Enter the taxon QID or scientific name below:":
        "Digite o QID do táxon ou o nome científico abaixo:",
      "Enter QID or scientific name": "Digite QID ou nome científico",
      "Username:": "Nome de usuário:",
      "Project name:": "Nome do projeto:",
      "Limit of observations (defaults to 200):":
        "Limite de observações (padrão 200):",
      "Wikipedia langcodes (defaults to 'en,pt'):":
        "Códigos de idioma da Wikipédia (padrão 'en,pt'):",
      "Research grade only?": "Apenas grau de pesquisa?",
      "Open license only?": "Apenas licença aberta?",
      Go: "Ir",
      "Loading observations...": "Carregando observações...",
      "Taxa seen by {name}": "Táxons vistos por {name}",
      "Taxa observed in the scope of the project \"{project}\"":
        "Táxons observados no escopo do projeto \"{project}\"",
      "Next {limit}": "Próximos {limit}",
      "Parsing up to {limit} most recent uploads (page {page}).":
        "Processando até {limit} envios mais recentes (página {page}).",
      Group: "Grupo",
      "Taxon Name": "Nome do táxon",
      "Number of observations": "Número de observações",
      "Observations by {name}": "Observações de {name}",
      "Wikidata ID": "ID do Wikidata",
      "Wikipages missing": "Páginas da Wikipédia ausentes",
      "create stub": "criar esboço",
      "Scientific name not found.": "Nome científico não encontrado.",
      "Generating stub...": "Gerando esboço...",
      "Stub for the Portuguese Wikipedia": "Esboço para a Wikipédia em português",
      "Stub for the Spanish Wikipedia": "Esboço para a Wikipédia em espanhol",
      "Stub for the English Wikipedia": "Esboço para a Wikipédia em inglês",
      "Stub for the French Wikipedia": "Esboço para a Wikipédia em francês",
      "Portuguese Wikipedia page:": "Página da Wikipédia em português:",
      "Spanish Wikipedia page:": "Página da Wikipédia em espanhol:",
      "English Wikipedia page:": "Página da Wikipédia em inglês:",
      "French Wikipedia page:": "Página da Wikipédia em francês:",
      "Powered by": "Alimentado por",
      "Code fully open source and open to contributions at the":
        "Código totalmente aberto e com contribuições no",
      "Special thanks to Andra Waagmeester and Dario Taraborelli for the guidance in the Open Biodiversity Knowledge / iNaturalist / eBird / Wiki / digital naturalism world.":
        "Agradecimentos especiais a Andra Waagmeester e Dario Taraborelli pela orientação no mundo do Open Biodiversity Knowledge / iNaturalist / eBird / Wiki / naturalismo digital.",
      "See also Andra's": "Veja também o",
      "for more cool stuff like this": "para mais coisas legais como esta",
      Contributors: "Contribuidores",
      "Your name will go here! :)": "Seu nome vai aparecer aqui! :)",
      "iNat2Wiki is a Flask App developed by Tiago Lubiana":
        "iNat2Wiki é um aplicativo Flask desenvolvido por Tiago Lubiana",
      "inspired by the": "inspirado pelo",
      "Taxa observed in the scope of the project":
        "Táxons observados no escopo do projeto",
      "An unexpected error (500) has occurred": "Ocorreu um erro inesperado (500)",
      "File Not Found (404)": "Arquivo não encontrado (404)",
      Back: "Voltar",
      "Something wrong happened! Maybe the user with id '{id}' does not exist?":
        "Algo deu errado! Talvez o usuário com id '{id}' não exista?",
      "Something wrong happened! Maybe the project with id '{id}' does not exist?":
        "Algo deu errado! Talvez o projeto com id '{id}' não exista?",
      "Failed to generate stub.": "Falha ao gerar o esboço.",
      Upload: "Enviar"
    }
  };

  const supportedLicenses = new Set(["cc-by", "cc-by-sa", "cc0"]);

  const legacyRoutes = new Set(["userlist", "projectlist", "wikistub", "about"]);

  const LANG_STRINGS = {
    pt: {
      taxonomia_header: "== Taxonomia ==",
      info_taxonomia: "{{Info/Taxonomia",
      ipni_link: "no Índice Internacional de Nomes de Plantas",
      reflora_link: "no projeto Flora e Funga do Brasil",
      bhl_link: "na Biodiversity Heritage Library",
      gbif_link: "no GBIF",
      inaturalist_link: "no iNaturalist",
      cnc_flora_link: "no portal do Centro Nacional de Conservação da Flora (Brasil)",
      leitura_adicional: "== Leitura adicional ==",
      taxon_described: "O táxon foi descrito oficialmente em",
      basionym_label: "basiônimo",
      e_join: " e "
    },
    en: {
      taxonomia_header: "== Taxonomy ==",
      info_taxonomia: "{{Info/Taxonomy",
      ipni_link: "in the International Plant Names Index",
      reflora_link: "in the Flora and Funga of Brazil project",
      bhl_link: "in the Biodiversity Heritage Library",
      gbif_link: "in GBIF",
      inaturalist_link: "in iNaturalist",
      cnc_flora_link: "on the National Center for Plant Conservation portal",
      leitura_adicional: "== Further reading ==",
      taxon_described: "The taxon was officially described in",
      basionym_label: "basionym",
      e_join: " and "
    },
    es: {
      taxonomia_header: "== Taxonomía ==",
      info_taxonomia: "{{Ficha de taxón",
      ipni_link: "en el Índice Internacional de Nombres de Plantas",
      reflora_link: "en el proyecto Flora y Funga de Brasil",
      bhl_link: "en la Biodiversity Heritage Library",
      gbif_link: "en GBIF",
      inaturalist_link: "en iNaturalist",
      cnc_flora_link: "en el portal del Centro Nacional de Conservación de la Flora (Brasil)",
      leitura_adicional: "== Lectura adicional ==",
      taxon_described: "El taxón fue descrito oficialmente en",
      basionym_label: "basónimo",
      e_join: " y "
    },
    fr: {
      taxonomia_header: "== Taxonomie ==",
      info_taxonomia: "{{Taxobox",
      ipni_link: "dans l'Index International des Noms de Plantes",
      reflora_link: "dans le projet Flora et Funga du Brésil",
      bhl_link: "dans la Biodiversity Heritage Library",
      gbif_link: "dans GBIF",
      inaturalist_link: "dans iNaturalist",
      cnc_flora_link: "sur le portail du Centre National de Conservation de la Flore (Brésil)",
      leitura_adicional: "== Lecture supplémentaire ==",
      taxon_described: "Le taxon a été officiellement décrit en",
      basionym_label: "basionym",
      e_join: " et "
    }
  };

  const WIKI_PAGE_SETTINGS = {
    pt: {
      title_format: "{{Título em itálico}}",
      stub_template: "{{esboço-biologia}}",
      references: "{{Referencias}}",
      external_heading: "== Ligações externas ==",
      authority: "{{Controle de autoridade}}",
      description: "é uma espécie",
      category_prefix: "[[Categoria:",
      family_prefix: "da família",
      genus_prefix: "do gênero",
      kingdom_text: "de planta "
    },
    en: {
      title_format: "{{Italic title}}",
      stub_template: "{{Biology-stub}}",
      references: "{{References}}",
      external_heading: "== External links ==",
      authority: "{{Authority control}}",
      description: "is a species",
      category_prefix: "[[Category:",
      family_prefix: "of the family",
      genus_prefix: "of the genus",
      kingdom_text: "of plant"
    },
    es: {
      title_format: "",
      stub_template: "",
      references: "==Referencias==\n{{listaref}}",
      external_heading: "== Enlaces externos ==",
      authority: "{{Control de autoridad}}",
      description: "es una especie",
      category_prefix: "[[Categoría:",
      family_prefix: "de la familia",
      genus_prefix: "del género",
      kingdom_text: "de planta"
    },
    fr: {
      title_format: "{{Titre en italique}}",
      stub_template: "{{Bio-stub}}",
      references: "{{Références}}",
      external_heading: "== Liens externes ==",
      authority: "{{Autorité de contrôle}}",
      description: "est une espèce",
      category_prefix: "[[Catégorie:",
      family_prefix: "de la famille",
      genus_prefix: "du genre",
      kingdom_text: "de plante"
    }
  };

  const BHL_LINK = {
    pt: "Documentos sobre",
    en: "Documents about",
    es: "Documentos sobre",
    fr: "Documents sur"
  };

  const BHL_SUFFIX = {
    pt: "na Biodiversity Heritage Library",
    en: "in the Biodiversity Heritage Library",
    es: "en la Biodiversity Heritage Library",
    fr: "dans la Biodiversity Heritage Library"
  };

  const INAT_LINK = {
    pt: "Observações de",
    en: "Observations of",
    es: "Observaciones de",
    fr: "Observations de"
  };

  const INAT_SUFFIX = {
    pt: "no iNaturalist",
    en: "in iNaturalist",
    es: "en iNaturalist",
    fr: "sur iNaturalist"
  };

  const GBIF_SUFFIX = {
    pt: "no GBIF",
    en: "in GBIF",
    es: "en GBIF",
    fr: "dans GBIF"
  };

  const BIRD_LINK_STRINGS = {
    pt: {
      wikiaves: "Página do Wikiaves sobre a",
      ebird: "Informações do eBird sobre a",
      xeno: "Vocalizações de",
      xeno_suffix: "no Xeno-canto"
    },
    en: {
      wikiaves: "Wikiaves page on",
      ebird: "eBird information on",
      xeno: "Vocalizations of",
      xeno_suffix: "on Xeno-canto"
    },
    es: {
      wikiaves: "Página de Wikiaves sobre",
      ebird: "Información de eBird sobre",
      xeno: "Vocalizaciones de",
      xeno_suffix: "en Xeno-canto"
    },
    fr: {
      wikiaves: "Page Wikiaves sur",
      ebird: "Informations eBird sur",
      xeno: "Vocalisations de",
      xeno_suffix: "sur Xeno-canto"
    }
  };

  const WIKISTUB_SYNONYM_HEADINGS = {
    pt: "=== Links externos para sinônimos ===",
    en: "=== External links for synonyms ===",
    es: "=== Enlaces externos para sinónimos ===",
    fr: "=== Liens externes pour synonymes ==="
  };

  const TAXONOMY_FIELD_LABELS = {
    pt: {
      kingdom: "reino",
      phylum: "filo",
      class: "classe",
      order: "ordem",
      family: "família",
      genus: "gênero",
      species: "espécie"
    },
    en: {
      kingdom: "kingdom",
      phylum: "phylum",
      class: "class",
      order: "order",
      family: "family",
      genus: "genus",
      species: "species"
    },
    es: {
      kingdom: "regnum",
      phylum: "phylum",
      class: "classis",
      order: "ordo",
      family: "familia",
      genus: "genus",
      species: "species"
    },
    fr: {
      kingdom: "règne",
      phylum: "embranchement",
      class: "classe",
      order: "ordre",
      family: "famille",
      genus: "genre",
      species: "espèce"
    }
  };

  let locale = "en";
  let navOpen = false;
  let showPrivacy = false;
  let route = { name: "index", observationId: null, query: {} };
  let previousPath = `${window.location.pathname}${window.location.search}` || "/";
  let observationId = "";
  let observationData = null;
  let qid = "";
  let errorPage = "";
  let legacyFlash = "";

  let userForm = {
    name: "",
    limit: "",
    langcodes: "",
    quality: true,
    license: true
  };
  let projectForm = {
    name: "",
    limit: "",
    langcodes: "",
    quality: true,
    license: true
  };

  let userInfo = null;
  let userSearchConfig = null;
  let userName = "";
  let userListLoading = false;

  let projectInfo = null;
  let projectSearchConfig = null;
  let projectName = "";
  let projectListLoading = false;

  let wikiStubInput = "";
  let wikiStubLoading = false;
  let wikiStubError = "";
  let wikiStubContent = "";
  let wikiStubQid = "";
  let wikiStubTaxonName = "";
  let wikiStubLang = "pt";

  let listError = "";

  const sparqlCache = new Map();

  function t(key) {
    const value = translations[locale]?.[key];
    if (value && value.length > 0) {
      return value;
    }
    return key;
  }

  function tParam(key, params = {}) {
    const value = t(key);
    return value.replace(/\{(\w+)\}/g, (match, token) => {
      if (params[token] === undefined || params[token] === null) {
        return match;
      }
      return String(params[token]);
    });
  }

  function pickBrowserLocale() {
    const languages = navigator.languages || [navigator.language || "en"];
    for (const lang of languages) {
      const short = lang.toLowerCase().split("-")[0];
      if (supportedLanguages.includes(short)) {
        return short;
      }
    }
    return "en";
  }

  function setLocale(lang) {
    if (!supportedLanguages.includes(lang)) {
      return;
    }
    locale = lang;
    localStorage.setItem("inat2wiki-lang", lang);
    document.documentElement.lang = lang;
  }

  function applyLocaleFromUrl(url) {
    const langParam = url.searchParams.get("lang");
    if (langParam && supportedLanguages.includes(langParam)) {
      setLocale(langParam);
      return;
    }

    const stored = localStorage.getItem("inat2wiki-lang");
    if (stored && supportedLanguages.includes(stored)) {
      setLocale(stored);
      return;
    }

    setLocale(pickBrowserLocale());
  }

  function parseRoute(url) {
    const pathname = url.pathname;
    const query = Object.fromEntries(url.searchParams.entries());

    if (pathname === "/" || pathname === "") {
      return { name: "index", observationId: null, query };
    }

    if (pathname === "/parse" || pathname === "/parse/") {
      return { name: "parse", observationId: null, query };
    }

    if (pathname.startsWith("/parse/")) {
      const parts = pathname.split("/").filter(Boolean);
      if (parts.length === 2) {
        return { name: "parse", observationId: parts[1], query };
      }
    }

    if (pathname === "/userlist" || pathname === "/userlist/") {
      return { name: "userlist", userId: null, query };
    }

    if (pathname.startsWith("/userlist/")) {
      const parts = pathname.split("/").filter(Boolean);
      if (parts.length === 2) {
        return { name: "userlist", userId: parts[1], query };
      }
    }

    if (pathname === "/projectlist" || pathname === "/projectlist/") {
      return { name: "projectlist", projectId: null, query };
    }

    if (pathname.startsWith("/projectlist/")) {
      const parts = pathname.split("/").filter(Boolean);
      if (parts.length === 2) {
        return { name: "projectlist", projectId: parts[1], query };
      }
    }

    if (pathname.startsWith("/wikistub/")) {
      const parts = pathname.split("/").filter(Boolean);
      if (parts.length >= 2) {
        return {
          name: "wikistub",
          lang: parts[1],
          identifier: parts.length >= 3 ? parts[2] : null,
          query
        };
      }
    }

    if (pathname === "/about") {
      return { name: "about", query };
    }

    if (pathname.startsWith("/set-lang/")) {
      const parts = pathname.split("/").filter(Boolean);
      if (parts.length === 2) {
        return { name: "set-lang", lang: parts[1], query };
      }
    }

    return { name: "notfound", query };
  }

  function handleNavigation() {
    const url = new URL(window.location.href);
    applyLocaleFromUrl(url);
    const nextRoute = parseRoute(url);

    if (nextRoute.name === "set-lang") {
      if (supportedLanguages.includes(nextRoute.lang)) {
        setLocale(nextRoute.lang);
      }
      const target =
        previousPath && !previousPath.startsWith("/set-lang/")
          ? previousPath
          : "/";
      window.history.replaceState({}, "", target);
      route = parseRoute(new URL(window.location.origin + target));
    } else {
      route = nextRoute;
    }

    navOpen = false;
    showPrivacy = false;
    errorPage = "";
    legacyFlash = "";
    listError = "";

    if (route.name === "parse" && route.observationId) {
      loadObservation(route.observationId);
    } else {
      observationData = null;
      qid = "";
    }

    if (route.name === "userlist" && route.userId) {
      loadUserList(route.userId, route.query);
    } else {
      userInfo = null;
      userSearchConfig = null;
      userName = "";
      userListLoading = false;
    }

    if (route.name === "projectlist" && route.projectId) {
      loadProjectList(route.projectId, route.query);
    } else {
      projectInfo = null;
      projectSearchConfig = null;
      projectName = "";
      projectListLoading = false;
    }

    if (route.name === "wikistub") {
      wikiStubLang = route.lang || "pt";
      if (route.identifier) {
        loadWikiStub(route.lang, route.identifier);
      } else {
        wikiStubContent = "";
        wikiStubQid = "";
        wikiStubTaxonName = "";
        wikiStubError = "";
        wikiStubLoading = false;
      }
    } else {
      wikiStubContent = "";
      wikiStubQid = "";
      wikiStubTaxonName = "";
      wikiStubError = "";
      wikiStubLoading = false;
    }
  }

  function navigate(path) {
    if (window.location.pathname === path) {
      return;
    }
    previousPath = `${window.location.pathname}${window.location.search}`;
    window.history.pushState({}, "", path);
    handleNavigation();
  }

  function normalizeObservationId(value) {
    if (!value) {
      return "";
    }
    if (value.includes("www.inaturalist.org/observations/")) {
      return value.split("/observations/").pop();
    }
    if (value.includes("inaturalist.org/observations/")) {
      return value.split("/observations/").pop();
    }
    return value.trim();
  }

  function submitObservation() {
    const cleaned = normalizeObservationId(observationId);
    if (!cleaned) {
      return;
    }
    navigate(`/parse/${cleaned}`);
  }

  function isLegacyRoute(name) {
    return legacyRoutes.has(name);
  }

  function parseSearchConfig(query) {
    return {
      page: parseInt(query.page || "1", 10) || 1,
      limit: parseInt(query.limit || "200", 10) || 200,
      quality_grade: query.quality_grade || "research",
      license: query.license || "cc0,cc-by,cc-by-sa",
      langcodes: query.langcodes || "en,pt"
    };
  }

  function buildRedirectFromForm(form, baseRoute) {
    if (!form.name.trim()) {
      return "";
    }
    const limit = form.limit ? parseInt(form.limit, 10) || 200 : 200;
    const qualityGrade = form.quality ? "research" : "any";
    const license = form.license ? "cc0,cc-by,cc-by-sa" : "any";
    const langcodes = form.langcodes ? form.langcodes : "pt,en";
    const params = new URLSearchParams({
      limit: String(limit),
      quality_grade: qualityGrade,
      license,
      langcodes
    });
    return `${baseRoute}/${encodeURIComponent(form.name.trim())}?${params.toString()}`;
  }

  function buildNextUrl(path, name, searchConfig) {
    const nextPage = searchConfig.page + 1;
    const params = new URLSearchParams({
      limit: String(searchConfig.limit),
      page: String(nextPage),
      quality_grade: searchConfig.quality_grade,
      license: searchConfig.license
    });
    return `/${path}/${encodeURIComponent(name)}?${params.toString()}`;
  }

  function submitUserList() {
    const url = buildRedirectFromForm(userForm, "/userlist");
    if (url) {
      navigate(url);
    }
  }

  function submitProjectList() {
    const url = buildRedirectFromForm(projectForm, "/projectlist");
    if (url) {
      navigate(url);
    }
  }

  function submitWikiStub() {
    if (!wikiStubInput.trim()) {
      return;
    }
    navigate(`/wikistub/${wikiStubLang}/${encodeURIComponent(wikiStubInput.trim())}`);
  }

  function togglePrivacy(event) {
    event.preventDefault();
    showPrivacy = !showPrivacy;
  }

  function handleLink(event, path) {
    event.preventDefault();
    navigate(path);
  }

  function handleLanguageChange(event) {
    navigate(`/set-lang/${event.target.value}`);
  }

  function handleOutsideClick(event) {
    const target = event.target;
    if (!target?.closest?.(".privacy-wrapper")) {
      showPrivacy = false;
    }
  }

  async function initializeDataTable() {
    await tick();
    const table = document.querySelector("#observations");
    if (!table || !window.$ || !window.$.fn || !window.$.fn.DataTable) {
      return;
    }
    const tableWrapper = window.$(table);
    if (window.$.fn.DataTable.isDataTable(table)) {
      tableWrapper.DataTable().destroy();
    }
    const languageUrls = {
      es: "https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json",
      pt: "https://cdn.datatables.net/plug-ins/1.10.25/i18n/Portuguese.json"
    };
    const options = {
      pageLength: 50,
      aaSorting: []
    };
    if (languageUrls[locale]) {
      options.language = { url: languageUrls[locale] };
    }
    tableWrapper.DataTable(options);
  }

  async function fetchSparql(query) {
    if (sparqlCache.has(query)) {
      return sparqlCache.get(query);
    }
    const url = `https://query.wikidata.org/sparql?format=json&query=${encodeURIComponent(
      query
    )}`;
    const promise = fetch(url, {
      headers: { Accept: "application/sparql-results+json" }
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("wikidata request failed");
        }
        return response.json();
      })
      .then((data) => data?.results?.bindings || []);
    sparqlCache.set(query, promise);
    return promise;
  }

  function formatValues(values) {
    const safeValues = values.filter(Boolean).map((value) => `"${value}"`);
    return `{ ${safeValues.join(" ")} }`;
  }

  function chunk(values, size) {
    const result = [];
    for (let i = 0; i < values.length; i += size) {
      result.push(values.slice(i, i + size));
    }
    return result;
  }

  async function lookupQid(taxonId) {
    if (!taxonId) {
      return "";
    }
    const query = `SELECT ?item WHERE { ?item wdt:P3151 "${taxonId}" . } LIMIT 1`;
    const bindings = await fetchSparql(query);
    const item = bindings?.[0]?.item?.value || "";
    return item ? item.split("/").pop() : "";
  }

  function buildUploadUrl(observation, photo, inatId) {
    const licenseMap = {
      "cc-by": "cc-by-4.0",
      "cc-by-sa": "cc-by-sa-4.0",
      cc0: "Cc-zero"
    };

    const license = licenseMap[photo.license_code];
    if (!license) {
      return "";
    }

    const photoUrl = (photo.url || "").replace("square", "original");
    const user = observation?.user || {};
    const userName = user?.name && user.name !== "" ? user.name : user.login_exact;
    const taxonName = observation?.taxon?.name || "";
    const title = `${taxonName} - ${userName} - ${photo.id}.jpeg`;

    let locationTemplate = "";
    if (observation?.geojson && observation?.taxon_geoprivacy === "open") {
      const lat = observation.geojson.coordinates[1];
      const lon = observation.geojson.coordinates[0];
      locationTemplate = `\n        {{Location|${lat}|${lon}|source:iNaturalist}}`;
    }

    const placeGuess = observation?.place_guess;
    const date = observation?.observed_on || "";
    const description = placeGuess
      ? `${taxonName}, ${placeGuess}, ${date} (iNaturalist).`
      : `${taxonName}, ${date} (iNaturalist).`;

    const summary = `{{Information\n        |description= ${description}\n        |date=${date}\n        |source=https://www.inaturalist.org/photos/${photo.id}\n        |author=[https://www.inaturalist.org/users/${user.id} ${userName}]\n        |permission=\n        |other versions=\n        }}${locationTemplate}\n\n        {{iNaturalist|${inatId}}}\n\n        {{INaturalistreview}}\n        [[Category:Media uploaded with inat2wiki]]\n        [[Category:${taxonName}]]`;

    const uploadPage = "https://commons.wikimedia.org/wiki/Special:Upload";
    const summaryForUrl = encodeURIComponent(summary);
    const titleForUrl = encodeURIComponent(title);

    return `${uploadPage}?wpUploadDescription=${summaryForUrl}&wpLicense=${license}&wpDestFile=${titleForUrl}&wpSourceType=url&wpUploadFileURL=${photoUrl}`;
  }

  async function loadObservation(inatId) {
    observationData = null;
    qid = "";
    errorPage = "";

    try {
      const response = await fetch(
        `https://api.inaturalist.org/v1/observations/${inatId}`
      );
      if (!response.ok) {
        throw new Error("request failed");
      }
      const data = await response.json();
      const observation = data?.results?.[0];
      if (!observation) {
        throw new Error("not found");
      }

      qid = await lookupQid(observation?.taxon?.min_species_taxon_id);

      const photos = (observation.photos || []).map((photo) => {
        const originalUrl = (photo.url || "").replace("square", "original");
        const uploadUrl = buildUploadUrl(observation, photo, inatId);
        return {
          ...photo,
          url: originalUrl,
          upload_url: uploadUrl
        };
      });

      observationData = { ...observation, photos };
    } catch (err) {
      errorPage = "500";
    }
  }

  function buildObservationsUrl(type, id, page, qualityGrade, license) {
    const url = new URL("https://api.inaturalist.org/v1/observations");
    if (type === "project") {
      url.searchParams.set("project_id", id);
    } else {
      url.searchParams.set("user_id", id);
    }
    url.searchParams.set("only_id", "false");
    url.searchParams.set("per_page", "200");
    url.searchParams.set("page", String(page));

    if (["research", "needs_id", "casual"].includes(qualityGrade)) {
      url.searchParams.set("quality_grade", qualityGrade);
    }
    if (["cc0", "cc-by", "cc-by-sa", "cc0,cc-by,cc-by-sa"].includes(license)) {
      url.searchParams.set("photo_license", license);
    }
    return url.toString();
  }

  async function extractCoreInformation(id, limit, qualityGrade, license, type, startingPage) {
    let coreInformation = {};
    let inaturalistTaxonIds = [];
    let totalCount = 0;
    let page = startingPage;

    while (totalCount < limit) {
      const url = buildObservationsUrl(type, id, page, qualityGrade, license);
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error("inat request failed");
      }
      const data = await response.json();
      const results = data?.results || [];
      if (!results.length) {
        break;
      }

      for (const obs of results) {
        if (!obs.taxon || !obs.taxon.min_species_taxon_id) {
          continue;
        }
        if (!obs.photos || obs.photos.length === 0) {
          continue;
        }
        const taxInfo = obs.taxon;
        const samplePhoto = obs.photos[0]?.url || "";
        const iconicName = taxInfo.iconic_taxon_name || "None";
        const licenseCode = obs.license_code;
        const speciesId = String(taxInfo.min_species_taxon_id);

        inaturalistTaxonIds.push(speciesId);

        const obsInfo = {
          id: obs.id,
          quality_grade: obs.quality_grade,
          license: licenseCode
        };

        if (coreInformation[speciesId]) {
          coreInformation[speciesId].observations.push(obsInfo);
        } else {
          coreInformation[speciesId] = {
            iconic_name: iconicName,
            sample_photo: samplePhoto,
            name: taxInfo.name,
            quality: obs.quality_grade,
            taxon_id: taxInfo.min_species_taxon_id,
            observations: [obsInfo]
          };
        }
      }

      totalCount += results.length;
      if (results.length < 200) {
        break;
      }
      page += 1;
    }

    inaturalistTaxonIds = inaturalistTaxonIds.slice(0, limit);
    coreInformation = Object.fromEntries(
      Object.entries(coreInformation).filter(([key]) => inaturalistTaxonIds.includes(key))
    );

    return { coreInformation, inaturalistTaxonIds };
  }

  async function addNumberOfObservationsPerTaxon(coreInformation, taxonIds) {
    const chunks = chunk(taxonIds, 30);
    await Promise.all(
      chunks.map(async (taxonChunk) => {
        const response = await fetch(
          `https://api.inaturalist.org/v1/taxa/${taxonChunk.join(",")}`
        );
        if (!response.ok) {
          return;
        }
        const data = await response.json();
        const results = data?.results || [];
        for (const taxonInfo of results) {
          const id = String(taxonInfo.id);
          if (coreInformation[id]) {
            coreInformation[id].number_of_observations = taxonInfo.observations_count;
          }
        }
      })
    );
  }

  async function addMissingImageData(coreInformation, taxonIds) {
    const formattedValues = formatValues(taxonIds);
    const query = `
    SELECT DISTINCT 
    (REPLACE(STR(?item), ".*Q", "Q") AS ?qid) 
    ?id
    ?image
    ?cc0_url
    ?ccby_url
    WHERE{
        VALUES ?id ${formattedValues}
        ?item wdt:P3151 ?id .
        OPTIONAL {?item wdt:P18 ?image} . 
        ?item rdfs:label ?itemLabel . 
        FILTER ( LANG(?itemLabel) = "en" )
        BIND(IRI(CONCAT(CONCAT("https://www.inaturalist.org/taxa/", ?id), "/browse_photos?photo_license=cc0")) AS ?cc0_url)
        BIND(IRI(CONCAT(CONCAT("https://www.inaturalist.org/taxa/", ?id), "/browse_photos?photo_license=cc-by")) AS ?ccby_url)
    }
    `;

    const results = await fetchSparql(query);
    for (const row of results) {
      const id = row.id?.value;
      if (!id || !coreInformation[id]) {
        continue;
      }
      coreInformation[id].wikidata_id = row.qid?.value || "";
      if (!row.image) {
        if (!coreInformation[id].wikipages_missing) {
          coreInformation[id].wikipages_missing = [];
        }
        if (!coreInformation[id].wikipages_missing.includes("wikidata_image")) {
          coreInformation[id].wikipages_missing.push("wikidata_image");
        }
      }
    }
  }

  async function addMissingWikipages(coreInformation, taxonIds, langcode) {
    const formattedValues = formatValues(taxonIds);
    const query = `
    SELECT DISTINCT * WHERE{
        VALUES ?id ${formattedValues}
            ?item wdt:P3151 ?id .
        ?item rdfs:label ?itemLabel . 
        FILTER ( LANG(?itemLabel) = "en" )
        MINUS{
        {?sitelink schema:about ?item .
        ?sitelink schema:isPartOf ?site.
        ?sitelink schema:isPartOf/wikibase:wikiGroup "wikipedia" .
        FILTER(CONTAINS(STR(?sitelink), "${langcode}.wiki"))}
                 }
        }    `;

    const results = await fetchSparql(query);
    for (const row of results) {
      const id = row.id?.value;
      if (!id || !coreInformation[id]) {
        continue;
      }
      if (!coreInformation[id].wikipages_missing) {
        coreInformation[id].wikipages_missing = [];
      }
      if (!coreInformation[id].wikipages_missing.includes(langcode)) {
        coreInformation[id].wikipages_missing.push(langcode);
      }
    }
  }

  async function loadObservationList(type, id, query) {
    const searchConfig = parseSearchConfig(query);
    const { coreInformation, inaturalistTaxonIds } = await extractCoreInformation(
      id,
      searchConfig.limit,
      searchConfig.quality_grade,
      searchConfig.license,
      type,
      searchConfig.page
    );

    if (Object.keys(coreInformation).length === 0) {
      throw new Error("not found");
    }

    await addNumberOfObservationsPerTaxon(coreInformation, inaturalistTaxonIds);

    const entries = Object.entries(coreInformation);
    for (const [, info] of entries) {
      if (info.number_of_observations === undefined) {
        info.number_of_observations = 0;
      }
    }

    entries.sort(
      (a, b) => (a[1].number_of_observations || 0) - (b[1].number_of_observations || 0)
    );

    const taxaIdsForQuery = entries.map(([idValue]) => idValue).slice(0, 100);
    await addMissingImageData(coreInformation, taxaIdsForQuery);

    const langcodes = searchConfig.langcodes
      .split(",")
      .map((value) => value.trim())
      .filter(Boolean);

    for (const langcode of langcodes) {
      await addMissingWikipages(coreInformation, taxaIdsForQuery, langcode);
    }

    return { entries, searchConfig };
  }

  async function loadUserList(id, query) {
    userListLoading = true;
    userInfo = null;
    userName = id;
    userSearchConfig = null;
    listError = "";
    legacyFlash = "";

    try {
      const { entries, searchConfig } = await loadObservationList("user", id, query);
      userInfo = entries;
      userSearchConfig = searchConfig;
      await initializeDataTable();
    } catch (err) {
      legacyFlash = tParam(
        "Something wrong happened! Maybe the user with id '{id}' does not exist?",
        { id }
      );
      listError = legacyFlash;
    } finally {
      userListLoading = false;
    }
  }

  async function loadProjectList(id, query) {
    projectListLoading = true;
    projectInfo = null;
    projectName = id;
    projectSearchConfig = null;
    listError = "";
    legacyFlash = "";

    try {
      const { entries, searchConfig } = await loadObservationList("project", id, query);
      projectInfo = entries;
      projectSearchConfig = searchConfig;
      await initializeDataTable();
    } catch (err) {
      legacyFlash = tParam(
        "Something wrong happened! Maybe the project with id '{id}' does not exist?",
        { id }
      );
      listError = legacyFlash;
    } finally {
      projectListLoading = false;
    }
  }

  function getBindingValue(binding, key) {
    return binding?.[key]?.value || "";
  }

  function uniqueValues(bindings, key) {
    const values = bindings
      .map((binding) => getBindingValue(binding, key))
      .filter((value) => value !== "");
    return [...new Set(values)];
  }

  async function resolveQidFromScientificName(name) {
    const query = `
    SELECT ?item WHERE {
      ?item wdt:P225 "${name}" .
    }
    LIMIT 1`;
    const bindings = await fetchSparql(query);
    const item = bindings?.[0]?.item?.value || "";
    return item ? item.split("/").pop() : "";
  }

  async function loadWikiStub(lang, identifier) {
    wikiStubLoading = true;
    wikiStubError = "";
    wikiStubContent = "";
    wikiStubQid = "";
    wikiStubTaxonName = "";

    const trimmed = identifier.trim();
    if (!trimmed) {
      wikiStubLoading = false;
      return;
    }

    const isQid = /^Q\d+$/i.test(trimmed);
    if (!isQid) {
      const resolvedQid = await resolveQidFromScientificName(trimmed);
      if (!resolvedQid) {
        wikiStubError = t("Scientific name not found.");
        wikiStubLoading = false;
        return;
      }
      navigate(`/wikistub/${lang}/${resolvedQid}`);
      return;
    }

    wikiStubQid = trimmed.toUpperCase();
    wikiStubLang = lang;

    try {
      const { stub, taxonName } = await buildWikiStub(wikiStubQid, wikiStubLang);
      wikiStubContent = stub;
      wikiStubTaxonName = taxonName;
    } catch (err) {
      wikiStubError = t("Failed to generate stub.");
    } finally {
      wikiStubLoading = false;
    }
  }

  async function getResultsData(qid) {
    const query = `
SELECT

?taxon_rankLabel
?parent_taxon
?parent_taxonLabel
?taxon_name
?taxon_author
?taxon_authorLabel
(YEAR(?description_date) as ?description_year)
?taxon_range_map_image
?taxon_common_name_pt
WHERE {
    VALUES ?taxon { wd:${qid} } .

    OPTIONAL { ?taxon wdt:P105 ?taxon_rank .
        ?taxon_rank rdfs:label ?taxon_rankLabel .
    FILTER(LANG(?taxon_rankLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P171 ?parent_taxon .
        ?parent_taxon rdfs:label ?parent_taxonLabel .
    FILTER(LANG(?parent_taxonLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P181 ?taxon_range_map_image } . 
    
    OPTIONAL { ?taxon wdt:P183 ?endemic_to .
        ?endemic_to rdfs:label ?endemic_toLabel .
    FILTER(LANG(?endemic_toLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P21 ?sex_or_gender .
        ?sex_or_gender rdfs:label ?sex_or_genderLabel .
    FILTER(LANG(?sex_or_genderLabel) = "en")} . 
    
    OPTIONAL { ?taxon p:P225 ?statement .
                ?statement ps:P225 ?taxon_name .
                OPTIONAL {?statement pq:P405 ?taxon_author . 
                ?statement pq:P574 ?description_date . 
                      ?taxon_author rdfs:label ?taxon_authorLabel .
    FILTER(LANG(?taxon_authorLabel) = "en")   }
    } . 
    
    OPTIONAL { ?taxon wdt:P10176 ?type_host .
        ?type_host rdfs:label ?type_hostLabel .
    FILTER(LANG(?type_hostLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P1034 ?main_food_source .
        ?main_food_source rdfs:label ?main_food_sourceLabel .
    FILTER(LANG(?main_food_sourceLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P1082 ?population .
        ?population rdfs:label ?populationLabel .
    FILTER(LANG(?populationLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P1606 ?natural_reservoir_of .
        ?natural_reservoir_of rdfs:label ?natural_reservoir_ofLabel .
    FILTER(LANG(?natural_reservoir_ofLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P1672 ?this_taxon_is_source_of .
        ?this_taxon_is_source_of rdfs:label ?this_taxon_is_source_ofLabel .
    FILTER(LANG(?this_taxon_is_source_ofLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P1843 ?taxon_common_name_pt .
    FILTER(LANG(?taxon_common_name_pt) = "pt")} . 
    
    OPTIONAL { ?taxon wdt:P2974 ?habitat .
        ?habitat rdfs:label ?habitatLabel .
    FILTER(LANG(?habitatLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P2975 ?host .
        ?host rdfs:label ?hostLabel .
    FILTER(LANG(?hostLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P3063 ?gestation_period .
        ?gestation_period rdfs:label ?gestation_periodLabel .
    FILTER(LANG(?gestation_periodLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P3492 ?basic_reproduction_number .
        ?basic_reproduction_number rdfs:label ?basic_reproduction_numberLabel .
    FILTER(LANG(?basic_reproduction_numberLabel) = "en")} . 
    
    OPTIONAL { ?taxon wdt:P427 ?taxonomic_type .
        ?taxonomic_type rdfs:label ?taxonomic_typeLabel .
    FILTER(LANG(?taxonomic_typeLabel) = "en")} . 
    

}`;
    return fetchSparql(query);
  }

  async function getParentTaxonData(qid, lang) {
    const query = `
    SELECT 
      ?taxonRank
      ?taxonRankLabel
      ?taxonName
      ?taxon_range_map_image
    WHERE {
      VALUES ?taxon { wd:${qid} } .
      ?taxon wdt:P171* ?parentTaxon.
      ?parentTaxon wdt:P105 ?taxonRank.
      ?parentTaxon wdt:P225 ?taxonName.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "${lang}". }
      OPTIONAL { ?taxon wdt:P181 ?taxon_range_map_image } .
    }`;

    return fetchSparql(query);
  }

  function getClassName(parentRows) {
    const classRow = parentRows.find(
      (row) => getBindingValue(row, "taxonRankLabel") === "classe"
    );
    if (classRow) {
      return getBindingValue(classRow, "taxonName");
    }
    const names = parentRows.map((row) => getBindingValue(row, "taxonName"));
    if (names.includes("Aves")) {
      return "Aves";
    }
    return "";
  }

  function getKingdomName(parentRows) {
    const kingdomRow = parentRows.find(
      (row) => getBindingValue(row, "taxonRank") === "http://www.wikidata.org/entity/Q36732"
    );
    return kingdomRow ? getBindingValue(kingdomRow, "taxonName") : "";
  }

  function getFamilyName(parentRows) {
    const familyRow = parentRows.find(
      (row) => getBindingValue(row, "taxonRank") === "http://www.wikidata.org/entity/Q35409"
    );
    return familyRow ? String(getBindingValue(familyRow, "taxonName")) : "";
  }

  function getGenusName(parentRows) {
    const genusRow = parentRows.find(
      (row) => getBindingValue(row, "taxonRank") === "http://www.wikidata.org/entity/Q34740"
    );
    return genusRow ? getBindingValue(genusRow, "taxonName") : "";
  }

  function getYearCategory(results, lang) {
    const year = getBindingValue(results[0] || {}, "description_year");
    if (!year) {
      return "";
    }
    const catLabels = {
      pt: `[[Categoria:Espécies descritas em ${year}]]`,
      en: `[[Category:Species described in ${year}]]`,
      es: `[[Categoría:Especies descritas en ${year}]]`,
      fr: `[[Catégorie:Espèces décrites en ${year}]]`
    };
    return catLabels[lang] || catLabels.pt;
  }

  function renderListWithoutDict(values) {
    let text = "";
    values.forEach((value, index) => {
      if (index === 0) {
        text += value;
      } else if (index === values.length - 1) {
        text += " e " + value;
      } else {
        text += ", " + value;
      }
    });
    return text;
  }

  async function fetchGbifClassification(qid) {
    const gbifId = await getGbifId(qid);
    if (!gbifId) {
      return null;
    }
    try {
      const response = await fetch(`https://api.gbif.org/v1/species/${gbifId}`);
      if (!response.ok) {
        return null;
      }
      const data = await response.json();
      return {
        gbifId,
        kingdom: data.kingdom || "",
        phylum: data.phylum || "",
        className: data.class || "",
        order: data.order || "",
        family: data.family || "",
        genus: data.genus || "",
        species: data.species || data.canonicalName || ""
      };
    } catch (err) {
      return null;
    }
  }

  function buildTaxoboxFromGbif(classification, lang) {
    const header = LANG_STRINGS[lang]?.info_taxonomia || LANG_STRINGS.pt.info_taxonomia;
    let result = `${header}\n`;
    result += "| imagem                = \n";

    if (!classification) {
      result += "}}";
      return result;
    }

    const labels = TAXONOMY_FIELD_LABELS[lang] || TAXONOMY_FIELD_LABELS.en;
    const entries = [
      ["kingdom", classification.kingdom],
      ["phylum", classification.phylum],
      ["class", classification.className],
      ["order", classification.order],
      ["family", classification.family],
      ["genus", classification.genus],
      ["species", classification.species]
    ];

    for (const [key, rawValue] of entries) {
      const value = rawValue ? String(rawValue).trim() : "";
      if (!value) {
        continue;
      }
      const label = labels[key] || key;
      const nSpace = 22 - label.length;
      const spacing = " ".repeat(Math.max(nSpace, 1));
      result += `| ${label}${spacing}= [[${value}]]\n`;
    }

    result += "}}";
    return result;
  }

  async function getGbifRef(qid, lang) {
    const query = `
    SELECT * WHERE { 
        wd:${qid} wdt:P846 ?gbif_id .
        wd:${qid} wdt:P225 ?taxon_name .
    }`;
    const results = await fetchSparql(query);
    if (!results.length) {
      return "";
    }
    const gbifId = getBindingValue(results[0], "gbif_id");
    const taxonName = getBindingValue(results[0], "taxon_name");
    if (!gbifId) {
      return "";
    }
    if (lang === "pt") {
      return `<ref>{{Citar web|url=https://www.gbif.org/species/${gbifId}|titulo=${taxonName}|acessodata=2022-04-18|website=www.gbif.org|lingua=en}}</ref>`;
    }
    if (lang === "en") {
      return `<ref>{{Cite web|url=https://www.gbif.org/species/${gbifId}|title=${taxonName}|access-date=2022-04-18|website=www.gbif.org}}</ref>`;
    }
    if (lang === "es") {
      return `<ref>{{Citar web|url=https://www.gbif.org/species/${gbifId}|título=${taxonName}|fechaacceso=2022-04-18|sitioweb=www.gbif.org}}</ref>`;
    }
    if (lang === "fr") {
      return `<ref>{{Citer web|url=https://www.gbif.org/species/${gbifId}|titre=${taxonName}|consulté_le=2022-04-18|site=www.gbif.org\n}}</ref>`;
    }
    return "";
  }

  async function getGbifId(qid) {
    const query = `
    SELECT * WHERE { 
        wd:${qid} wdt:P846 ?gbif_id .
    }`;
    const results = await fetchSparql(query);
    return results.length ? getBindingValue(results[0], "gbif_id") : "";
  }

  async function getRefloraId(qid) {
    const query = `
    SELECT * WHERE { 
        wd:${qid} wdt:P10701 ?reflora_id .
    }`;
    const results = await fetchSparql(query);
    return results.length ? getBindingValue(results[0], "reflora_id") : "";
  }

  async function getInaturalistId(qid) {
    const query = `
    SELECT * WHERE { 
        wd:${qid} wdt:P3151 ?inaturalist_id .
    }`;
    const results = await fetchSparql(query);
    return results.length ? getBindingValue(results[0], "inaturalist_id") : "";
  }

  async function getIpniId(qid) {
    const query = `
    SELECT * WHERE { 
        wd:${qid} wdt:P961 ?ipni_id .
    }`;
    const results = await fetchSparql(query);
    return results.length ? getBindingValue(results[0], "ipni_id") : "";
  }

  async function renderRefloraLink(taxonName, qid, lang) {
    const refloraId = await getRefloraId(qid);
    if (!refloraId) {
      return "";
    }
    const phrase = LANG_STRINGS[lang]?.reflora_link || LANG_STRINGS.pt.reflora_link;
    return `* [http://reflora.jbrj.gov.br/reflora/listaBrasil/FichaPublicaTaxonUC/FichaPublicaTaxonUC.do?id=${refloraId} ''${taxonName}'' ${phrase}]`;
  }

  async function renderIpniLink(taxonName, qid, lang) {
    const ipniId = await getIpniId(qid);
    if (!ipniId) {
      return "";
    }
    const phrase = LANG_STRINGS[lang]?.ipni_link || LANG_STRINGS.pt.ipni_link;
    return `* [https://www.ipni.org/n/${ipniId} ''${taxonName}'' ${phrase}.]`;
  }

  function renderCncFlora(taxonName, lang) {
    const phrase = LANG_STRINGS[lang]?.cnc_flora_link || LANG_STRINGS.pt.cnc_flora_link;
    return `* [http://cncflora.jbrj.gov.br/portal/pt-br/profile/${encodeURIComponent(
      taxonName
    )} ''${taxonName}'' ${phrase}]`;
  }

  function renderBhl(taxonName, lang) {
    const prefix = BHL_LINK[lang] || BHL_LINK.pt;
    const suffix = BHL_SUFFIX[lang] || BHL_SUFFIX.pt;
    return `* [https://www.biodiversitylibrary.org/name/${encodeURIComponent(
      taxonName
    )} ${prefix} ''${taxonName}'' ${suffix}]`;
  }

  async function renderInaturalist(taxonName, qid, lang) {
    const inatId = await getInaturalistId(qid);
    if (!inatId) {
      return "";
    }
    const prefix = INAT_LINK[lang] || INAT_LINK.pt;
    const suffix = INAT_SUFFIX[lang] || INAT_SUFFIX.pt;
    return `* [https://www.inaturalist.org/taxa/${inatId} ${prefix} ''${taxonName}'' ${suffix}]`;
  }

  async function renderGbif(taxonName, qid, lang) {
    const gbifId = await getGbifId(qid);
    if (!gbifId) {
      return "";
    }
    const suffix = GBIF_SUFFIX[lang] || GBIF_SUFFIX.pt;
    return `* [https://www.gbif.org/species/${gbifId} ''${taxonName}'' ${suffix}]`;
  }

  async function renderAdditionalReading(qid, lang) {
    const query = `
    SELECT * WHERE { 
        ?article wdt:P921 wd:${qid} .
    }`;
    const results = await fetchSparql(query);
    if (!results.length || !results[0]["article"]) {
      return "";
    }
    const header = LANG_STRINGS[lang]?.leitura_adicional || LANG_STRINGS.pt.leitura_adicional;
    let text = header;
    for (const row of results) {
      if (row.article?.value) {
        text += `\n  * {{ Citar Q | ${qid} }}`;
      }
    }
    return text;
  }

  async function checkIfHasBasionym(qid) {
    const query = `
    SELECT * WHERE {
        wd:${qid} wdt:P566 ?basionym .
    }`;
    const results = await fetchSparql(query);
    const value = results?.[0]?.basionym?.value || "";
    return value ? value.split("/").pop() : "";
  }

  async function renderTaxonomy(results, qid, lang) {
    const strings = LANG_STRINGS[lang] || LANG_STRINGS.pt;
    let description = "";
    const authorLabels = uniqueValues(results, "taxon_authorLabel");
    const descriptionYear = getBindingValue(results[0] || {}, "description_year");

    if (authorLabels.length && descriptionYear) {
      const formatted = authorLabels.map((name) => `[[${name}]]`);
      description = `${strings.taxon_described} [[${descriptionYear}]] por ${renderListWithoutDict(
        formatted
      )}. ${await getGbifRef(qid, lang)}`;
    }

    let text = `\n${description}\n`;
    const basionymQid = await checkIfHasBasionym(qid);

    if (basionymQid) {
      const basionymResults = await getResultsData(basionymQid);
      const basionymAuthors = uniqueValues(basionymResults, "taxon_authorLabel");
      const basionymYear = getBindingValue(basionymResults[0] || {}, "description_year");
      const basionymName = getBindingValue(basionymResults[0] || {}, "taxon_name");
      const basionymParent = getBindingValue(basionymResults[0] || {}, "parent_taxonLabel");
      const basionymFormatted = basionymAuthors.map((name) => `[[${name}]]`);

      if (lang === "pt") {
        text += `\nA espécie havia sido descrita anteriormente sob o [[${strings.basionym_label}]] '''''${basionymName}''''' (gênero ''[[${basionymParent}]]'') em ${basionymYear} por ${renderListWithoutDict(
          basionymFormatted
        )}. ${await getGbifRef(basionymQid, lang)}\n`;
      } else if (lang === "en") {
        text += `\nThe species had been previously described under the [[${strings.basionym_label}]] '''''${basionymName}''''' (genus ''[[${basionymParent}]]'') in ${basionymYear} by ${renderListWithoutDict(
          basionymFormatted
        )}. ${await getGbifRef(basionymQid, lang)}\n`;
      } else if (lang === "es") {
        text += `\nLa especie había sido descrita anteriormente bajo el [[${strings.basionym_label}]] '''''${basionymName}''''' (género ''[[${basionymParent}]]'') en ${basionymYear} por ${renderListWithoutDict(
          basionymFormatted
        )}. ${await getGbifRef(basionymQid, lang)}\n`;
      } else if (lang === "fr") {
        text += `\nL'espèce avait été décrite précédemment sous le [[${strings.basionym_label}]] '''''${basionymName}''''' (genre ''[[${basionymParent}]]'') en ${basionymYear} par ${renderListWithoutDict(
          basionymFormatted
        )}. ${await getGbifRef(basionymQid, lang)}\n`;
      }
    }

    if (text.trim() === "") {
      return "";
    }
    return `\n${strings.taxonomia_header}\n${text}`;
  }

  async function getBirdLinks(qid, lang) {
    const query = `
    SELECT ?wiki_aves_bird_id ?ebird_taxon_id ?xeno_canto_species_id ?bird_label WHERE {
      wd:${qid} wdt:P4664 ?wiki_aves_bird_id.
      wd:${qid} wdt:P3444 ?ebird_taxon_id.
      wd:${qid} wdt:P2426 ?xeno_canto_species_id.
      OPTIONAL {
        wd:${qid} rdfs:label ?bird_label.
        FILTER (lang(?bird_label) = "${lang}").
      }
    }`;
    const results = await fetchSparql(query);
    if (!results.length) {
      return "";
    }
    const row = results[0];
    const strings = BIRD_LINK_STRINGS[lang] || BIRD_LINK_STRINGS.pt;
    const wikiaves = getBindingValue(row, "wiki_aves_bird_id");
    const ebird = getBindingValue(row, "ebird_taxon_id");
    const xeno = getBindingValue(row, "xeno_canto_species_id");
    const birdLabel = (getBindingValue(row, "bird_label") || "essa ave").toLowerCase();

    if (!wikiaves || !ebird || !xeno) {
      return "";
    }

    return `
* [https://www.wikiaves.com.br/wiki/${wikiaves} ${strings.wikiaves} ${birdLabel}]
* [https://ebird.org/species/${ebird} ${strings.ebird} ${birdLabel}]
* [https://www.xeno-canto.org/species/${xeno} ${strings.xeno} ${birdLabel} ${strings.xeno_suffix}]`;
  }

  async function renderExternalLinks(taxonName, qid, birdLinks, externalHeading, lang) {
    let text = `
${externalHeading}
${await renderRefloraLink(taxonName, qid, lang)}
${await renderIpniLink(taxonName, qid, lang)}
${renderCncFlora(taxonName, lang)}
${renderBhl(taxonName, lang)}
${await renderInaturalist(taxonName, qid, lang)}
${await renderGbif(taxonName, qid, lang)}
${birdLinks}
    `;

    const basionymQid = await checkIfHasBasionym(qid);
    if (basionymQid) {
      const basionymResults = await getResultsData(basionymQid);
      const basionymName = getBindingValue(basionymResults[0] || {}, "taxon_name");
      const heading = WIKISTUB_SYNONYM_HEADINGS[lang] || WIKISTUB_SYNONYM_HEADINGS.en;
      text += `
${heading}
${await renderRefloraLink(basionymName, basionymQid, lang)}
${renderBhl(basionymName, lang)}
${await renderInaturalist(basionymName, basionymQid, lang)}
${await renderGbif(basionymName, basionymQid, lang)}
`;
    }

    return text;
  }

  function normalizeWikitext(text) {
    return text.replace(/\n\n+/g, "\n").replace(/^ /gm, "");
  }

  async function buildWikiStub(qid, lang) {
    const results = await getResultsData(qid);
    if (!results.length) {
      throw new Error("No Wikidata results");
    }
    const taxonName = getBindingValue(results[0], "taxon_name");
    const classification = await fetchGbifClassification(qid);
    const kingdom = classification?.kingdom || "";
    const className = classification?.className || "";
    const family = classification?.family || "";
    const genus =
      classification?.genus ||
      (classification?.species ? classification.species.split(" ")[0] : "") ||
      taxonName;
    const yearCategory = getYearCategory(results, lang);
    const settings = WIKI_PAGE_SETTINGS[lang] || WIKI_PAGE_SETTINGS.pt;
    const taxobox = buildTaxoboxFromGbif(classification, lang);

    const familySentence = family
      ? ` ${settings.family_prefix} [[${family}]]${LANG_STRINGS[lang]?.e_join || ""}`
      : "";

    const birdLinks = className === "Aves" ? await getBirdLinks(qid, lang) : "";
    const kingdomText = kingdom === "Plantae" ? settings.kingdom_text : "";

    const externalLinks = await renderExternalLinks(
      taxonName,
      qid,
      birdLinks,
      settings.external_heading,
      lang
    );

    const taxonomy = await renderTaxonomy(results, qid, lang);
    const additionalReading = await renderAdditionalReading(qid, lang);
    const gbifRef = await getGbifRef(qid, lang);

    let wikiPage = `
${settings.title_format}
${taxobox}
'''''${taxonName}''''' ${settings.description} ${kingdomText}${familySentence}${settings.genus_prefix} ''[[${genus}]]''.  ${gbifRef}
${taxonomy}
${settings.references}
${externalLinks}
${additionalReading}
${settings.authority}
${settings.stub_template}
${settings.category_prefix}${genus}]]${yearCategory}`;

    wikiPage = normalizeWikitext(wikiPage);

    return { stub: wikiPage, taxonName };
  }

  onMount(() => {
    handleNavigation();
    window.addEventListener("popstate", handleNavigation);
    document.addEventListener("click", handleOutsideClick);
  });

  onDestroy(() => {
    window.removeEventListener("popstate", handleNavigation);
    document.removeEventListener("click", handleOutsideClick);
  });
</script>

<div class="d-flex flex-column min-vh-100" style="background-color: var(--lightest-green);">
  <nav class="navbar navbar-expand-md navbar-light bg-light border">
    <a class="navbar-brand" href="/" on:click|preventDefault={(event) => handleLink(event, "/")}
      ><img src="/logo.png" width="55" alt={t("iNat2Wiki Logo")} /> iNat2Wiki</a
    >
    <button
      class="navbar-toggler"
      type="button"
      aria-controls="navbar"
      aria-expanded={navOpen}
      aria-label={t("Toggle navigation")}
      on:click={() => (navOpen = !navOpen)}
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" class:show={navOpen} id="navbar">
      <ul class="navbar-nav mr-auto mt-2">
        <li class="nav-item">
          <a
            class="nav-link"
            href="/userlist"
            on:click|preventDefault={(event) => handleLink(event, "/userlist")}
            >{t("User list")}</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            href="/projectlist"
            on:click|preventDefault={(event) => handleLink(event, "/projectlist")}
            >{t("Project list")}</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            href="/parse"
            on:click|preventDefault={(event) => handleLink(event, "/parse")}
            >{t("Parse observation")}</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            href="/wikistub/pt"
            on:click|preventDefault={(event) => handleLink(event, "/wikistub/pt")}
            >{t("Portuguese Wikipedia Stub")}</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            href="/about"
            on:click|preventDefault={(event) => handleLink(event, "/about")}
            >{t("About")}</a
          >
        </li>
      </ul>
      <div class="d-flex align-items-center ml-md-auto mt-2 mt-md-0">
        <label class="sr-only" for="language-select">{t("Language")}</label>
        <select
          id="language-select"
          class="custom-select custom-select-sm"
          bind:value={locale}
          on:change={handleLanguageChange}
        >
          <option value="en">English</option>
          <option value="pt">Português</option>
          <option value="es">Español</option>
        </select>
      </div>
    </div>
  </nav>

  {#if isLegacyRoute(route.name)}
    <header>
      {#if legacyFlash}
        <div class="alert alert-primary border text-center" role="alert">
          {legacyFlash}
        </div>
      {/if}
    </header>
  {/if}

  <main class={`container-fluid ${isLegacyRoute(route.name) ? "mt-2" : "mt-4 mb-5"} flex-grow-1`}>
    {#if isLegacyRoute(route.name)}
      <div class="alert alert-warning text-center" role="alert">
        🚧 {t("This tool is being rebuilt! Check out the new version at")}{" "}
        <a href="https://inat2wiki-dev.toolforge.org" class="alert-link"
          >inat2wiki-dev.toolforge.org</a
        >
        {t("and leave feedback or feature requests on the")}{" "}
        <a href="https://github.com/lubianat/inat2wiki-dev" class="alert-link"
          >{t("GitHub repository")}</a
        >.
      </div>
    {/if}

    <div class="row justify-content-center">
      <div class="col-12 col-md-10 col-lg-8">
        {#if errorPage === "500"}
          <h1>{t("An unexpected error (500) has occurred")}</h1>
          <p>
            <a href="/" on:click|preventDefault={(event) => handleLink(event, "/")}
              >{t("Back")}</a
            >
          </p>
        {:else if route.name === "notfound"}
          <h1>{t("File Not Found (404)")}</h1>
          <p>
            <a href="/" on:click|preventDefault={(event) => handleLink(event, "/")}
              >{t("Back")}</a
            >
          </p>
        {:else if route.name === "index"}
          <div class="container">
            <p>{t("iNat2Wiki is an interface between iNaturalist and Wikimedia projects.")}</p>
            <p>
              {t(
                "This is a slow rewrite of the original tool, with a single goal of adding pictures of particular observations to commons via"
              )}
              "
              <a href="/parse" on:click|preventDefault={(event) => handleLink(event, "/parse")}
                >{t("Parse observation")}</a
              >"
            </p>
          </div>
        {:else if route.name === "parse"}
          {#if !observationData}
            <h4>{t("Enter the observation id")}: </h4>
            <form on:submit|preventDefault={submitObservation}>
              <input name="obs_id" bind:value={observationId} />
              <input type="submit" value={t("Submit")} />
            </form>
            <a
              href="/parse/144917694"
              on:click|preventDefault={(event) => handleLink(event, "/parse/144917694")}
              >{t("See an example")}</a
            >
          {/if}

          {#if observationData}
            <div class="col-md container">
              <h3>
                {t("Observation")} {observationData.id} ({observationData.taxon?.name})
              </h3>
              <ul>
                <li>
                  {t("Wikidata page")}: <a
                    href={`https://www.wikidata.org/entity/${qid}`}
                    target="_blank"
                    rel="noreferrer"
                    >{qid}</a
                  >
                </li>
                <li>
                  {t("Observation on iNaturalist")}: <a
                    href={`https://inaturalist.org/observations/${observationData.id}`}
                    target="_blank"
                    rel="noreferrer"
                    >{observationData.id}</a
                  >
                </li>
              </ul>

              <table class="table table-striped">
                <thead>
                  <tr>
                    <th>{t("Image")}</th>
                    <th>{t("License")}</th>
                    <th>{t("Link to Commons")}</th>
                  </tr>
                </thead>
                <tbody>
                  {#each observationData.photos as photo}
                    <tr>
                      <td><img src={photo.url} width="300" alt={t("Observation")} /></td>
                      <td>{t("License")}: {photo.license_code}</td>
                      <td>
                        {#if supportedLicenses.has(photo.license_code)}
                          <a
                            href={photo.upload_url}
                            target="blank"
                            class="btn btn-outline-primary"
                            role="button"
                            >{t("Upload to Commons")}</a
                          >
                        {:else}
                          <p>{t("License not supported")}</p>
                        {/if}
                      </td>
                    </tr>
                  {/each}
                </tbody>
              </table>
            </div>
          {/if}
        {:else if route.name === "userlist"}
          {#if !userInfo && !userListLoading}
            <h4>{t("Enter the iNaturalist username below:")}</h4>
            <form on:submit|preventDefault={submitUserList} class="needs-validation" novalidate>
              <div class="mb-3">
                <label class="form-label">{t("Username:")}</label>
                <input class="form-control" bind:value={userForm.name} required />
              </div>
              <div class="mb-3">
                <label class="form-label">{t("Limit of observations (defaults to 200):")}</label>
                <input class="form-control" type="number" bind:value={userForm.limit} />
              </div>
              <div class="mb-3">
                <label class="form-label">{t("Wikipedia langcodes (defaults to 'en,pt'):")}</label>
                <input class="form-control" bind:value={userForm.langcodes} />
              </div>
              <div class="mb-3">
                <label class="form-label">
                  <input type="checkbox" bind:checked={userForm.quality} /> {t("Research grade only?")}
                </label>
              </div>
              <div class="mb-3">
                <label class="form-label">
                  <input type="checkbox" bind:checked={userForm.license} /> {t("Open license only?")}
                </label>
              </div>
              <button type="submit" class="btn btn-primary">{t("Go")}</button>
            </form>
            <a href="/userlist/ramarese" on:click|preventDefault={(event) => handleLink(event, "/userlist/ramarese")}
              >{t("See an example")}</a
            >
          {/if}

          {#if userListLoading}
            <p>{t("Loading observations...")}</p>
          {/if}

          {#if userInfo}
            <div class="row">
              <div class="col-md container">
                <h3>{tParam("Taxa seen by {name}", { name: userName })}</h3>
                <button class="btn btn-outline-primary pager float-right">
                  <a
                    href={buildNextUrl("userlist", userName, userSearchConfig)}
                    on:click|preventDefault={(event) =>
                      handleLink(event, buildNextUrl("userlist", userName, userSearchConfig))}
                    >{tParam("Next {limit}", { limit: userSearchConfig.limit })}</a
                  >
                </button>
                <p>
                  {tParam("Parsing up to {limit} most recent uploads (page {page}).", {
                    limit: userSearchConfig.limit,
                    page: userSearchConfig.page
                  })}
                </p>
                <table id="observations" class="table table-striped">
                  <thead>
                    <tr>
                      <th>{t("Image")}</th>
                      <th>{t("Group")}</th>
                      <th>{t("Taxon Name")}</th>
                      <th>{t("Number of observations")}</th>
                      <th>{tParam("Observations by {name}", { name: userName })}</th>
                      <th>{t("Wikidata ID")}</th>
                      <th>{t("Wikipages missing")}</th>
                    </tr>
                  </thead>
                  <tbody>
                    {#each userInfo as [taxonId, taxonInfo]}
                      <tr>
                        <td><img src={taxonInfo.sample_photo} alt={taxonInfo.name} /></td>
                        <td>{taxonInfo.iconic_name}</td>
                        <td>{taxonInfo.name}</td>
                        <td>{taxonInfo.number_of_observations}</td>
                        <td>
                          {#each taxonInfo.observations as obs, idx}
                            {obs.id}
                            [
                            <a
                              href={`https://www.inaturalist.org/observations/${obs.id}`}
                              target="_blank"
                              rel="noreferrer"
                              >iNat</a
                            >,
                            <a
                              href={`/parse/${obs.id}`}
                              target="_blank"
                              rel="noreferrer"
                              >{t("Upload")}</a
                            >]
                            ({obs.quality_grade}; {obs.license}){idx <
                            taxonInfo.observations.length - 1
                              ? ", "
                              : ""}
                          {/each}
                        </td>
                        <td>
                          {#if taxonInfo.wikidata_id}
                            <a
                              href={`http://www.wikidata.org/entity/${taxonInfo.wikidata_id}`}
                              target="_blank"
                              rel="noreferrer"
                              >{taxonInfo.wikidata_id}</a
                            >
                          {/if}
                        </td>
                        <td>
                          {#if taxonInfo.wikipages_missing}
                            {#each taxonInfo.wikipages_missing as wikiPage, idx}
                              {#if wikiPage === "pt"}
                                {wikiPage} (
                                <a
                                  href={`/wikistub/pt/${taxonInfo.wikidata_id}`}
                                  target="_blank"
                                  rel="noreferrer"
                                  >{t("create stub")}</a
                                >
                                ){idx < taxonInfo.wikipages_missing.length - 1 ? ", " : ""}
                              {:else}
                                {wikiPage}{idx < taxonInfo.wikipages_missing.length - 1 ? ", " : ""}
                              {/if}
                            {/each}
                          {/if}
                        </td>
                      </tr>
                    {/each}
                  </tbody>
                </table>
              </div>
            </div>
          {/if}
        {:else if route.name === "projectlist"}
          {#if !projectInfo && !projectListLoading}
            <h4>{t("Enter the iNaturalist project name below:")}</h4>
            <form on:submit|preventDefault={submitProjectList} class="needs-validation" novalidate>
              <div class="mb-3">
                <label class="form-label">{t("Project name:")}</label>
                <input class="form-control" bind:value={projectForm.name} required />
              </div>
              <div class="mb-3">
                <label class="form-label">{t("Limit of observations (defaults to 200):")}</label>
                <input class="form-control" type="number" bind:value={projectForm.limit} />
              </div>
              <div class="mb-3">
                <label class="form-label">{t("Wikipedia langcodes (defaults to 'en,pt'):")}</label>
                <input class="form-control" bind:value={projectForm.langcodes} />
              </div>
              <div class="mb-3">
                <label class="form-label">
                  <input type="checkbox" bind:checked={projectForm.quality} /> {t("Research grade only?")}
                </label>
              </div>
              <div class="mb-3">
                <label class="form-label">
                  <input type="checkbox" bind:checked={projectForm.license} /> {t("Open license only?")}
                </label>
              </div>
              <button type="submit" class="btn btn-primary">{t("Go")}</button>
            </form>
            <a
              href="/projectlist/wikiproject-biodiversity"
              on:click|preventDefault={(event) =>
                handleLink(event, "/projectlist/wikiproject-biodiversity")}
              >{t("See an example")}</a
            >
          {/if}

          {#if projectListLoading}
            <p>{t("Loading observations...")}</p>
          {/if}

          {#if projectInfo}
            <div class="row">
              <div class="col-md container">
                <h3>
                  {tParam("Taxa observed in the scope of the project \"{project}\"", {
                    project: projectName
                  })}
                </h3>
                <button class="btn btn-outline-primary pager float-right">
                  <a
                    href={buildNextUrl("projectlist", projectName, projectSearchConfig)}
                    on:click|preventDefault={(event) =>
                      handleLink(event, buildNextUrl("projectlist", projectName, projectSearchConfig))}
                    >{tParam("Next {limit}", { limit: projectSearchConfig.limit })}</a
                  >
                </button>
                <p>
                  {tParam("Parsing up to {limit} most recent uploads (page {page}).", {
                    limit: projectSearchConfig.limit,
                    page: projectSearchConfig.page
                  })}
                </p>
                <table id="observations" class="table table-striped">
                  <thead>
                    <tr>
                      <th>{t("Image")}</th>
                      <th>{t("Group")}</th>
                      <th>{t("Taxon Name")}</th>
                      <th>{t("Number of observations")}</th>
                      <th>{tParam("Observations by {name}", { name: projectName })}</th>
                      <th>{t("Wikidata ID")}</th>
                      <th>{t("Wikipages missing")}</th>
                    </tr>
                  </thead>
                  <tbody>
                    {#each projectInfo as [taxonId, taxonInfo]}
                      <tr>
                        <td><img src={taxonInfo.sample_photo} alt={taxonInfo.name} /></td>
                        <td>{taxonInfo.iconic_name}</td>
                        <td>{taxonInfo.name}</td>
                        <td>{taxonInfo.number_of_observations}</td>
                        <td>
                          {#each taxonInfo.observations as obs, idx}
                            {obs.id}
                            [
                            <a
                              href={`https://www.inaturalist.org/observations/${obs.id}`}
                              target="_blank"
                              rel="noreferrer"
                              >iNat</a
                            >,
                            <a
                              href={`/parse/${obs.id}`}
                              target="_blank"
                              rel="noreferrer"
                              >{t("Upload")}</a
                            >]
                            ({obs.quality_grade}; {obs.license}){idx <
                            taxonInfo.observations.length - 1
                              ? ", "
                              : ""}
                          {/each}
                        </td>
                        <td>
                          {#if taxonInfo.wikidata_id}
                            <a
                              href={`http://www.wikidata.org/entity/${taxonInfo.wikidata_id}`}
                              target="_blank"
                              rel="noreferrer"
                              >{taxonInfo.wikidata_id}</a
                            >
                          {/if}
                        </td>
                        <td>
                          {#if taxonInfo.wikipages_missing}
                            {#each taxonInfo.wikipages_missing as wikiPage, idx}
                              {#if wikiPage === "pt"}
                                {wikiPage} (
                                <a
                                  href={`/wikistub/pt/${taxonInfo.wikidata_id}`}
                                  target="_blank"
                                  rel="noreferrer"
                                  >{t("create stub")}</a
                                >
                                ){idx < taxonInfo.wikipages_missing.length - 1 ? ", " : ""}
                              {:else}
                                {wikiPage}{idx < taxonInfo.wikipages_missing.length - 1 ? ", " : ""}
                              {/if}
                            {/each}
                          {/if}
                        </td>
                      </tr>
                    {/each}
                  </tbody>
                </table>
              </div>
            </div>
          {/if}
        {:else if route.name === "wikistub"}
          {#if !wikiStubContent && !wikiStubLoading}
            <h4>{t("Enter the taxon QID or scientific name below:")}</h4>
            <form on:submit|preventDefault={submitWikiStub}>
              <input
                name="taxon_identifier"
                placeholder={t("Enter QID or scientific name")}
                bind:value={wikiStubInput}
              />
              <input type="submit" value={t("Submit")} />
            </form>

            {#if wikiStubError}
              <div class="alert alert-danger">
                {wikiStubError}
              </div>
            {/if}

            <a
              href={`/wikistub/${wikiStubLang}/Q50713950`}
              on:click|preventDefault={(event) =>
                handleLink(event, `/wikistub/${wikiStubLang}/Q50713950`)}
              >{t("See an example")}</a
            >
          {/if}

          {#if wikiStubLoading}
            <p>{t("Generating stub...")}</p>
          {/if}

          {#if wikiStubContent}
            <div class="col-md container">
              {#if wikiStubLang === "pt"}
                <h3>{t("Stub for the Portuguese Wikipedia")}</h3>
                <ul>
                  <li>
                    {t("Wikidata page")}:
                    <a
                      href={`https://www.wikidata.org/entity/${wikiStubQid}`}
                      target="_blank"
                      rel="noreferrer"
                      >{wikiStubQid}</a
                    >
                  </li>
                  <li>
                    {t("Portuguese Wikipedia page:")}
                    <a
                      href={`https://pt.wikipedia.org/w/index.php?title=${wikiStubTaxonName}&action=edit`}
                      target="_blank"
                      rel="noreferrer"
                      >https://pt.wikipedia.org/wiki/{wikiStubTaxonName}</a
                    >
                  </li>
                </ul>
              {:else if wikiStubLang === "es"}
                <h3>{t("Stub for the Spanish Wikipedia")}</h3>
                <ul>
                  <li>
                    {t("Wikidata page")}:
                    <a
                      href={`https://www.wikidata.org/entity/${wikiStubQid}`}
                      target="_blank"
                      rel="noreferrer"
                      >{wikiStubQid}</a
                    >
                  </li>
                  <li>
                    {t("Spanish Wikipedia page:")}
                    <a
                      href={`https://es.wikipedia.org/w/index.php?title=${wikiStubTaxonName}&action=edit`}
                      target="_blank"
                      rel="noreferrer"
                      >https://es.wikipedia.org/wiki/{wikiStubTaxonName}</a
                    >
                  </li>
                </ul>
              {:else if wikiStubLang === "en"}
                <h3>{t("Stub for the English Wikipedia")}</h3>
                <ul>
                  <li>
                    {t("Wikidata page")}:
                    <a
                      href={`https://www.wikidata.org/entity/${wikiStubQid}`}
                      target="_blank"
                      rel="noreferrer"
                      >{wikiStubQid}</a
                    >
                  </li>
                  <li>
                    {t("English Wikipedia page:")}
                    <a
                      href={`https://en.wikipedia.org/w/index.php?title=${wikiStubTaxonName}&action=edit`}
                      target="_blank"
                      rel="noreferrer"
                      >https://en.wikipedia.org/wiki/{wikiStubTaxonName}</a
                    >
                  </li>
                </ul>
              {:else if wikiStubLang === "fr"}
                <h3>{t("Stub for the French Wikipedia")}</h3>
                <ul>
                  <li>
                    {t("Wikidata page")}:
                    <a
                      href={`https://www.wikidata.org/entity/${wikiStubQid}`}
                      target="_blank"
                      rel="noreferrer"
                      >{wikiStubQid}</a
                    >
                  </li>
                  <li>
                    {t("French Wikipedia page:")}
                    <a
                      href={`https://fr.wikipedia.org/w/index.php?title=${wikiStubTaxonName}&action=edit`}
                      target="_blank"
                      rel="noreferrer"
                      >https://fr.wikipedia.org/wiki/{wikiStubTaxonName}</a
                    >
                  </li>
                </ul>
              {/if}
              <pre>
{wikiStubContent}
              </pre>
            </div>
          {/if}
        {:else if route.name === "about"}
          <div class="container">
            <h3>{t("About")}</h3>
            <p>
              {t("iNat2Wiki is a Flask App developed by Tiago Lubiana")}
              (<a href="https://github.com/lubianat" target="_blank" rel="noreferrer">@lubianat</a>)
              {t("inspired by the")}
              <a
                href="https://www.wikidata.org/wiki/Wikidata:WikiProject_Biodiversity"
                target="_blank"
                rel="noreferrer"
              >
                WikiProject Biodiversity.
              </a>
            </p>

            <p>
              {t("Code fully open source and open to contributions at the")}
              <a href="https://github.com/lubianat/inat2wiki" target="_blank" rel="noreferrer">
                iNat2Wiki {t("GitHub repository")}
              </a>.
            </p>
            <p>
              {t(
                "Special thanks to Andra Waagmeester and Dario Taraborelli for the guidance in the Open Biodiversity Knowledge / iNaturalist / eBird / Wiki / digital naturalism world."
              )}
            </p>

            <p>
              {t("See also Andra's")}
              <a
                href="https://github.com/wikiproject-biodiversity?"
                target="_blank"
                rel="noreferrer"
              >
                https://github.com/wikiproject-biodiversity
              </a>
              {t("for more cool stuff like this")}
            </p>

            <h4>{t("Contributors")}</h4>
            <ul>
              <li>{t("Your name will go here! :)")}</li>
            </ul>
          </div>
        {/if}
      </div>
    </div>
  </main>

  {#if isLegacyRoute(route.name)}
    <footer class="small text-center text-muted">
      {t("Powered by")}
      <a href="https://www.wikidata.org/wiki/Wikidata:Main_Page">Wikidata</a>.
      {t("Code and feedback in the")}
      <a href="https://github.com/lubianat/inat2wiki"> {t("GitHub repository")}</a>.
    </footer>
  {:else}
    <footer class="small text-center text-muted mt-4 mb-3">
      {t("Code and feedback in the")}
      <a href="https://github.com/lubianat/inat2wiki-dev">{t("GitHub repository")}</a>.
      <span class="privacy-wrapper ml-2">
        <a href="#" role="button" on:click={togglePrivacy}>{t("Privacy")}</a>
        {#if showPrivacy}
          <div class="privacy-popover" role="dialog" aria-label={t("Privacy & Cookies")}>
            <h6>{t("Privacy & Cookies")}</h6>
            <p>
              {t("We set one first‑party cookie called")} <code>session</code>
              {t(
                "to remember your language choice. It expires when you close your browser and is never shared. No tracking, no analytics."
              )}
            </p>
          </div>
        {/if}
      </span>
    </footer>
  {/if}
</div>
