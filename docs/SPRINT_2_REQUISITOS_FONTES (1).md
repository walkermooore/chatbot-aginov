**SPRINT 2**

**Requisitos e fontes institucionais**

| **Campo**     | **Descrição**                                                    |
|---------------|------------------------------------------------------------------|
| Projeto       | Chatbot informacional para apoio ao atendimento da AGINOV/UNEMAT |
| Subprojeto    | Análise de requisitos, projeto e testes                          |
| Sprint        | Sprint 2 — Requisitos e fontes institucionais                    |
| Status        | Versão inicial para validação                                    |
| Base anterior | Sprint 1 — Fundamentação e protocolo de pesquisa                 |

*Documento gerado para acompanhamento da Sprint 2 e validação com orientadora e representantes autorizados da AGINOV.*

# 1. Objetivo

Entender usuários, demandas informacionais, restrições institucionais e fontes confiáveis que deverão orientar a base de conhecimento do chatbot informacional da AGINOV/UNEMAT.

A Sprint 2 dá continuidade à Sprint 1, que delimitou o chatbot como MVP informacional, com respostas baseadas em conteúdo aprovado, fontes oficiais, fallback, encaminhamento para canais oficiais, registro mínimo de perguntas não respondidas e cuidados com privacidade.

# 2. Entregas previstas

- Perfis de usuários e jornadas essenciais.

- Requisitos funcionais e não funcionais priorizados.

- Inventário de páginas, documentos e canais oficiais.

- Categorias candidatas e amostra de perguntas frequentes.

- Matriz de rastreabilidade entre fonte, assunto e responsável pela revisão.

# 3. Critérios de aceite

| **ID** | **Critério de aceite**                                            | **Forma de verificação**                                                                         | **Situação**  |
|--------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|---------------|
| CA01   | Requisitos são verificáveis.                                      | Cada requisito possui identificador, descrição, prioridade e critério de aceite.                 | Em elaboração |
| CA02   | Toda resposta candidata possui origem identificada.               | Cada pergunta/resposta candidata aponta fonte oficial, documento, página ou canal.               | Em elaboração |
| CA03   | Pendências de autorização estão separadas do conteúdo utilizável. | A matriz classifica conteúdo como utilizável, pendente ou não utilizável.                        | Em elaboração |
| CA04   | Perfis de usuários e jornadas essenciais estão descritos.         | Há jornadas para estudante, pesquisador/professor, empresa/setor produtivo e comunidade externa. | Em elaboração |
| CA05   | Categorias candidatas estão alinhadas às fontes institucionais.   | Cada categoria possui fonte associada ou pendência registrada.                                   | Em elaboração |
| CA06   | Responsáveis pela revisão estão indicados ou pendentes.           | A matriz informa responsável sugerido, setor ou pendência de definição.                          | Em elaboração |

# 4. Perfis de usuários

| **ID** | **Perfil**                 | **Necessidades informacionais**                                                                              | **Riscos de atendimento**                                                              | **Encaminhamento esperado**                                          |
|--------|----------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| PU01   | Estudante                  | Capacitações, eventos, empreendedorismo, inovação, editais e canais de apoio.                                | Interpretar informação geral como inscrição confirmada ou prazo garantido.             | Página oficial, edital vigente ou canal oficial.                     |
| PU02   | Pesquisador/professor      | Proteção de criações, comunicado de invenção, software, marca, parceria, PD&I e transferência de tecnologia. | Enviar detalhes sigilosos da invenção ou esperar parecer técnico pelo chatbot.         | Formulário oficial ou atendimento humano da AGINOV.                  |
| PU03   | Inventor independente      | Possibilidade de atendimento, serviços técnicos, orientação inicial e canais de contato.                     | Solicitar análise de viabilidade, parecer jurídico ou protocolo pelo chatbot.          | Canal oficial da AGINOV, sem coleta de documentos no chat.           |
| PU04   | Empresa ou setor produtivo | Parcerias, licenciamento, portfólio tecnológico, PD&I e contato institucional.                               | Entender resposta como promessa de negociação, aprovação ou disponibilidade comercial. | Contato institucional e fonte oficial sobre transferência/portfólio. |
| PU05   | Comunidade externa         | Informações gerais sobre AGINOV, eventos, serviços e formas de contato.                                      | Receber orientação desatualizada sobre evento, prazo ou responsável.                   | Página oficial atualizada ou fallback com canal humano.              |
| PU06   | Equipe AGINOV              | Reduzir dúvidas repetitivas, manter respostas, revisar fontes e acompanhar lacunas.                          | Publicar conteúdo sem validação ou deixar links/prazos vencidos ativos.                | Área administrativa simples e matriz de revisão.                     |

# 5. Jornadas essenciais

### J01 — Estudante busca evento ou capacitação

| **Etapa** | **Ação do usuário**                                    | **Resposta esperada do chatbot**                                                 | **Observação**                       |
|-----------|--------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------|
| 1         | Abre o chatbot.                                        | Saudação, identificação como assistente virtual e aviso de limite institucional. | Obrigatório no MVP.                  |
| 2         | Pergunta sobre eventos, capacitações ou oportunidades. | Busca conteúdo vigente na base.                                                  | Só responder se houver fonte e data. |
| 3         | Conteúdo validado existe.                              | Exibe resposta resumida, fonte oficial e data de atualização.                    | Não prometer inscrição ou vaga.      |
| 4         | Conteúdo não validado ou vencido.                      | Aciona fallback e encaminha ao canal oficial.                                    | Não gerar resposta livre.            |

### J02 — Pesquisador quer proteger uma criação

| **Etapa** | **Ação do usuário**                                           | **Resposta esperada do chatbot**                                     | **Observação**                  |
|-----------|---------------------------------------------------------------|----------------------------------------------------------------------|---------------------------------|
| 1         | Pergunta como registrar patente, software, marca ou cultivar. | Explica apenas orientação inicial e aponta fonte/formulário oficial. | Não emitir parecer.             |
| 2         | Usuário tenta enviar detalhes técnicos.                       | Alerta para não informar dados sigilosos ou confidenciais.           | Minimização de dados.           |
| 3         | Dúvida exige avaliação.                                       | Encaminha para atendimento humano da AGINOV.                         | Não receber documentos no chat. |

### J03 — Empresa busca parceria ou licenciamento

| **Etapa** | **Ação do usuário**                               | **Resposta esperada do chatbot**                                                                       | **Observação**                           |
|-----------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------|
| 1         | Pergunta sobre parceria ou tecnologia disponível. | Apresenta orientação geral sobre PD&I, transferência ou vitrine tecnológica, se houver fonte validada. | Resposta informacional.                  |
| 2         | Pergunta sobre negociação ou aprovação.           | Informa que a negociação depende de contato com a AGINOV.                                              | Não tomar decisão.                       |
| 3         | Precisa continuar atendimento.                    | Aponta canal oficial ou página institucional.                                                          | Registrar dúvida se não houver resposta. |

### J04 — Usuário faz pergunta fora do escopo

| **Etapa** | **Ação do usuário**                           | **Resposta esperada do chatbot**                                            | **Observação**                |
|-----------|-----------------------------------------------|-----------------------------------------------------------------------------|-------------------------------|
| 1         | Pergunta sobre tema não relacionado à AGINOV. | Informa limitação do assistente.                                            | Fallback.                     |
| 2         | Usuário insiste ou pergunta algo sensível.    | Não gera resposta conclusiva e encaminha ao canal adequado quando possível. | Segurança e LGPD.             |
| 3         | Registro.                                     | Registra lacuna de forma mínima ou categorizada.                            | Sem identificação do usuário. |

# 6. Requisitos priorizados da Sprint 2

### 6.1 Requisitos funcionais

| **ID**   | **Requisito**                                                                                          | **Prioridade** | **Critério de aceite**                                                                 | **Situação** |
|----------|--------------------------------------------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------|--------------|
| RF-S2-01 | Recuperar respostas apenas de conteúdos ativos, aprovados e com fonte identificada.                    | Must           | Conteúdo sem fonte, vencido, suspenso ou não validado não é usado em resposta pública. | A validar    |
| RF-S2-02 | Apresentar fonte oficial e data de atualização quando a resposta depender de informação institucional. | Must           | Resposta mostra fonte, link ou identificação do documento/canal e data de revisão.     | A validar    |
| RF-S2-03 | Acionar fallback quando não houver conteúdo validado para a dúvida do usuário.                         | Must           | Perguntas sem resposta aprovada geram mensagem de limitação e encaminhamento.          | A validar    |
| RF-S2-04 | Registrar perguntas não respondidas de forma minimizada, sem exigir identificação do usuário.          | Must           | Registro contém data, categoria estimada e texto minimizado/categorizado.              | A validar    |
| RF-S2-05 | Permitir classificação da base por categoria, criticidade, status, fonte e responsável pela revisão.   | Must           | Cada item da base possui campos mínimos de rastreabilidade.                            | A validar    |
| RF-S2-06 | Permitir atualização de conteúdos institucionais sem alteração direta no código-fonte.                 | Must           | Usuário autorizado consegue cadastrar, editar, aprovar, suspender ou revisar conteúdo. | A validar    |
| RF-S2-07 | Separar conteúdo utilizável, conteúdo pendente de validação e conteúdo não utilizável.                 | Must           | A base ou matriz possui status visível para cada fonte/resposta candidata.             | A validar    |
| RF-S2-08 | Permitir avaliação simples da resposta pelo usuário.                                                   | Must           | Voto “útil” ou “não útil” é registrado sem identificação pessoal.                      | A validar    |

### 6.2 Requisitos não funcionais

| **ID**    | **Atributo**            | **Requisito**                                                                                                   | **Prioridade** | **Critério de aceite**                                           |
|-----------|-------------------------|-----------------------------------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------|
| RNF-S2-01 | Rastreabilidade         | Toda resposta candidata deverá estar vinculada a fonte, assunto, status e responsável ou pendência de revisão.  | Must           | Matriz preenchida para todas as respostas candidatas.            |
| RNF-S2-02 | Atualidade              | Conteúdos sobre editais, eventos, prazos, contatos e formulários deverão possuir data de revisão.               | Must           | Conteúdo sem data de revisão não é classificado como utilizável. |
| RNF-S2-03 | Segurança institucional | O chatbot não deverá emitir parecer técnico, jurídico ou administrativo.                                        | Must           | Perguntas de decisão, análise ou protocolo geram encaminhamento. |
| RNF-S2-04 | Privacidade             | O chatbot não deverá solicitar CPF, matrícula, telefone, endereço, senha ou documentos pessoais no uso público. | Must           | Fluxos de atendimento não pedem identificação.                   |
| RNF-S2-05 | Clareza                 | Respostas candidatas deverão usar linguagem simples e indicar limites do atendimento automatizado.              | Must           | Rubrica de revisão confirma clareza e limite institucional.      |
| RNF-S2-06 | Manutenibilidade        | Conteúdos institucionais deverão ser organizados em estrutura atualizável.                                      | Must           | Base permite edição sem alteração do código-fonte.               |

# 7. Inventário inicial de fontes institucionais

Legenda de status:

- **Utilizável como fonte candidata:** fonte oficial localizada, mas ainda depende de validação da AGINOV antes de entrar na base pública.

- **Pendente de validação:** fonte localizada, mas precisa de confirmação de atualidade, responsável ou autorização.

- **Não utilizável como resposta:** fonte pode servir como contexto, mas não deve gerar resposta pública.

| **ID** | **Fonte institucional**                              | **Tipo**                        | **Assuntos relacionados**                                                           | **Conteúdo candidato**                                                     | **Status**                      | **Responsável pela revisão** |
|--------|------------------------------------------------------|---------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------|---------------------------------|------------------------------|
| FI01   | Página “Quem somos” da AGINOV/UNEMAT                 | Página institucional            | Sobre a AGINOV, missão, públicos atendidos                                          | Apresentação da Agência e finalidade institucional.                        | Utilizável como fonte candidata | AGINOV — a definir           |
| FI02   | Página “O que fazemos” da AGINOV/UNEMAT              | Página institucional            | Atribuições, PI, TT, inovação, empreendedorismo, serviços                           | Explicação geral das atribuições da AGINOV.                                | Utilizável como fonte candidata | AGINOV — a definir           |
| FI03   | Página “Propriedade Intelectual”                     | Página institucional            | Patentes e conceitos iniciais de PI                                                 | Orientação geral sobre patentes e tipos de proteção.                       | Pendente de validação           | AGINOV — PI                  |
| FI04   | Página “Formulários”                                 | Página institucional/documentos | Relatório de invenção, marca, software, cultivar, desenho industrial, requerimentos | Encaminhamento para formulários oficiais, sem receber arquivos no chatbot. | Utilizável como fonte candidata | AGINOV — PI                  |
| FI05   | Página “Transferência de Tecnologia”                 | Página institucional            | Licenciamento, tecnologias da UNEMAT, negociação com AGINOV                         | Orientação inicial sobre licenciamento e contato para negociação.          | Utilizável como fonte candidata | AGINOV — TT                  |
| FI06   | Página “Vitrine Tecnológica”                         | Página institucional/documentos | Portfólio tecnológico, tecnologias disponíveis, edições do portfólio                | Encaminhamento para consulta ao portfólio/vitrine.                         | Utilizável como fonte candidata | AGINOV — TT                  |
| FI07   | Página “Pesquisa, Desenvolvimento e Inovação — PD&I” | Página institucional            | Parcerias, acordos, convênios, setor produtivo                                      | Orientação inicial sobre instrumentos de parceria.                         | Utilizável como fonte candidata | AGINOV — PD&I                |
| FI08   | Página “Serviços Técnicos Especializados”            | Página institucional            | Serviços técnicos, assistência técnica, inventores independentes                    | Explicação geral e encaminhamento para atendimento.                        | Pendente de validação           | AGINOV — a definir           |
| FI09   | Página institucional nova da AGINOV                  | Página institucional            | Sobre, equipe, contatos e comitê técnico                                            | Contatos e estrutura institucional.                                        | Pendente de validação           | AGINOV — diretoria           |
| FI10   | Editais e notícias da UNEMAT                         | Página institucional dinâmica   | Eventos, oportunidades e chamadas                                                   | Respostas somente quando houver publicação vigente.                        | Pendente de validação contínua  | AGINOV/UNEMAT — a definir    |

# 8. Categorias candidatas

| **ID** | **Categoria**                        | **Descrição**                                                                    | **Fonte principal** | **Status**                     |
|--------|--------------------------------------|----------------------------------------------------------------------------------|---------------------|--------------------------------|
| C01    | Sobre a AGINOV                       | Missão, atuação, públicos atendidos, vínculo institucional e canais.             | FI01, FI02, FI09    | Candidata                      |
| C02    | Propriedade intelectual              | Patentes, software, marcas, desenho industrial, cultivares e orientação inicial. | FI03, FI04          | Candidata                      |
| C03    | Comunicado de invenção e formulários | Localização de formulários e orientação geral, sem envio de documentos no chat.  | FI04                | Candidata                      |
| C04    | Transferência de tecnologia          | Licenciamento, vitrine tecnológica e contato para negociação.                    | FI05, FI06          | Candidata                      |
| C05    | Parcerias e PD&I                     | Acordos, convênios, setor produtivo e projetos de inovação.                      | FI07                | Candidata                      |
| C06    | Serviços técnicos especializados     | Serviços técnicos e atendimento inicial a inventores/criadores independentes.    | FI08                | Candidata                      |
| C07    | Empreendedorismo e inovação          | Capacitações, ambientes promotores, startups, empresas juniores e eventos.       | FI02, FI10          | Pendente de validação          |
| C08    | Editais, eventos e oportunidades     | Divulgação apenas com fonte vigente e data de atualização.                       | FI10                | Pendente de validação contínua |
| C09    | Contato e atendimento humano         | Canais oficiais e situações que exigem análise da equipe.                        | FI01, FI02, FI09    | Candidata                      |

# 9. Amostra inicial de perguntas frequentes candidatas

As respostas abaixo são candidatas. Elas não devem ser publicadas no chatbot sem validação da AGINOV.

| **ID** | **Categoria**               | **Pergunta candidata**                                        | **Tipo de resposta esperada**                                                                                     | **Fonte**                               | **Status**                     |
|--------|-----------------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------|--------------------------------|
| FAQ01  | Sobre a AGINOV              | O que é a AGINOV?                                             | Explicar que é o Núcleo de Inovação Tecnológica da UNEMAT e resumir sua missão.                                   | FI01, FI09                              | Candidata                      |
| FAQ02  | Sobre a AGINOV              | Quem pode procurar a AGINOV?                                  | Informar públicos gerais: pesquisadores, estudantes, empresas, instituições e comunidade externa, conforme fonte. | FI01, FI09                              | Candidata                      |
| FAQ03  | Propriedade intelectual     | A AGINOV registra patente para mim pelo chatbot?              | Informar que o chatbot não protocola pedidos e encaminhar ao canal/formulário oficial.                            | FI03, FI04                              | Candidata                      |
| FAQ04  | Formulários                 | Onde encontro o formulário de relatório de invenção?          | Apontar a página de formulários, sem receber arquivo pelo chatbot.                                                | FI04                                    | Candidata                      |
| FAQ05  | Propriedade intelectual     | Posso enviar detalhes da minha invenção pelo chat?            | Orientar a não enviar informações sigilosas e encaminhar ao canal oficial.                                        | FI04 + regra de privacidade da Sprint 1 | Candidata                      |
| FAQ06  | Transferência de tecnologia | Como uma empresa pode licenciar uma tecnologia da UNEMAT?     | Explicar orientação inicial e encaminhar para transferência/vitrine e contato oficial.                            | FI05, FI06                              | Candidata                      |
| FAQ07  | Vitrine tecnológica         | Onde vejo as tecnologias disponíveis da UNEMAT?               | Encaminhar para a vitrine tecnológica/portfólio.                                                                  | FI06                                    | Candidata                      |
| FAQ08  | PD&I                        | Como propor parceria de pesquisa, desenvolvimento e inovação? | Explicar de forma inicial que existem instrumentos como acordos/parcerias/convênios, com encaminhamento.          | FI07                                    | Candidata                      |
| FAQ09  | Serviços técnicos           | A AGINOV atende inventor independente?                        | Informar apenas orientação geral conforme fonte e encaminhar para contato oficial.                                | FI08                                    | Pendente de validação          |
| FAQ10  | Eventos                     | Há editais ou eventos abertos?                                | Responder somente se houver fonte vigente; caso contrário, indicar canal oficial.                                 | FI10                                    | Pendente de validação contínua |
| FAQ11  | Atendimento humano          | Como falar com a AGINOV?                                      | Apresentar canal oficial validado.                                                                                | FI01, FI02, FI09                        | Pendente de confirmação        |
| FAQ12  | Fora do escopo              | O chatbot pode aprovar minha proposta ou interpretar edital?  | Informar limitação e encaminhar para canal oficial.                                                               | Regras de negócio da Sprint 1           | Candidata                      |

# 10. Matriz de rastreabilidade entre fonte, assunto e responsável

| **Fonte** | **Assunto**                          | **Categoria**           | **FAQ associada**   | **Criticidade** | **Status**                     | **Responsável pela revisão** |
|-----------|--------------------------------------|-------------------------|---------------------|-----------------|--------------------------------|------------------------------|
| FI01      | Missão e apresentação da AGINOV      | C01                     | FAQ01, FAQ02        | Média           | Candidata                      | AGINOV — a definir           |
| FI02      | Atribuições da AGINOV                | C01, C02, C04, C05, C07 | FAQ01, FAQ02, FAQ08 | Alta            | Candidata                      | AGINOV — a definir           |
| FI03      | Conceitos de propriedade intelectual | C02                     | FAQ03               | Alta            | Pendente de validação          | AGINOV — PI                  |
| FI04      | Formulários oficiais                 | C03                     | FAQ04, FAQ05        | Crítica         | Candidata                      | AGINOV — PI                  |
| FI05      | Transferência de tecnologia          | C04                     | FAQ06               | Alta            | Candidata                      | AGINOV — TT                  |
| FI06      | Vitrine tecnológica/portfólio        | C04                     | FAQ07               | Média           | Candidata                      | AGINOV — TT                  |
| FI07      | PD&I e parcerias                     | C05                     | FAQ08               | Alta            | Candidata                      | AGINOV — PD&I                |
| FI08      | Serviços técnicos especializados     | C06                     | FAQ09               | Alta            | Pendente de validação          | AGINOV — a definir           |
| FI09      | Contatos e equipe                    | C01, C09                | FAQ11               | Alta            | Pendente de confirmação        | AGINOV — diretoria           |
| FI10      | Editais, eventos e oportunidades     | C08                     | FAQ10               | Crítica         | Pendente de validação contínua | AGINOV/UNEMAT — a definir    |

# 11. Conteúdo utilizável, pendente e não utilizável

### 11.1 Conteúdo candidato utilizável após validação

- Apresentação geral da AGINOV.

- Atribuições gerais da Agência.

- Encaminhamento para página de formulários.

- Encaminhamento para transferência de tecnologia.

- Encaminhamento para vitrine tecnológica.

- Encaminhamento para PD&I e parcerias.

- Encaminhamento para atendimento humano.

### 11.2 Conteúdo pendente de autorização ou confirmação

- Contatos atualizados que devem aparecer no chatbot.

- Nome de responsáveis institucionais.

- Procedimento atualizado para cada formulário.

- Política de revisão e validade de conteúdos.

- Procedimento para dúvidas de inventores independentes.

- Fontes de editais, eventos e oportunidades vigentes.

- Responsável institucional por cada categoria.

### 11.3 Conteúdo não utilizável como resposta automática

- Parecer técnico ou jurídico sobre criação.

- Interpretação definitiva de edital.

- Confirmação de inscrição, aprovação, prazo ou protocolo.

- Recebimento de documentos, contratos ou arquivos técnicos.

- Análise de anterioridade, viabilidade ou classificação de propriedade intelectual.

- Respostas sem fonte oficial ou com conteúdo vencido.

# 12. Pendências da Sprint 2

| **ID**  | **Pendência**                                                             | **Encaminhamento**                          |
|---------|---------------------------------------------------------------------------|---------------------------------------------|
| P-S2-01 | Validar categorias candidatas com a AGINOV.                               | Reunião ou formulário de validação.         |
| P-S2-02 | Confirmar quais contatos oficiais podem aparecer no chatbot.              | Validação com responsável institucional.    |
| P-S2-03 | Definir responsável por revisão de cada categoria.                        | Matriz de responsáveis.                     |
| P-S2-04 | Confirmar política de retenção de perguntas não respondidas.              | Alinhar com orientação institucional/LGPD.  |
| P-S2-05 | Confirmar se haverá entrevistas ou testes com participantes nesta sprint. | Consultar orientação ética antes da coleta. |
| P-S2-06 | Validar amostra inicial de perguntas frequentes.                          | Revisão por representante autorizado.       |
| P-S2-07 | Separar conteúdo vigente de conteúdo apenas contextual.                   | Revisão da matriz de fontes.                |

# 13. Próximos passos

1.  Revisar este documento com a orientadora.

2.  Enviar a matriz de fontes e categorias para validação da AGINOV.

3.  Confirmar responsáveis institucionais por categoria.

4.  Ajustar RFs, RNFs e RCs conforme validação.

5.  Transformar perguntas frequentes candidatas em base inicial validada.

6.  Registrar pendências e emitir a versão 1.1 da Sprint 2.

# 14. Referências institucionais consultadas

As fontes abaixo foram usadas apenas para compor o inventário inicial. O conteúdo final do chatbot dependerá de validação institucional.

- AGINOV/UNEMAT — Quem somos: https://unemat.br/site/aginov/quem-somos

- AGINOV/UNEMAT — O que fazemos: https://unemat.br/site/aginov/o-que-fazemos

- AGINOV/UNEMAT — Propriedade Intelectual: https://unemat.br/site/aginov/propriedade-intelectual

- AGINOV/UNEMAT — Formulários: https://unemat.br/site/aginov/formularios

- AGINOV/UNEMAT — Transferência de Tecnologia: https://unemat.br/site/aginov/transferencia-de-tecnologia

- AGINOV/UNEMAT — Vitrine Tecnológica: https://unemat.br/site/aginov/vitrine-tecnologica

- AGINOV/UNEMAT — Pesquisa, Desenvolvimento e Inovação — PD&I: https://unemat.br/site/aginov/pesquisa-desenvolvimento-e-inovacao-pdi

- AGINOV/UNEMAT — Serviços Técnicos Especializados: https://unemat.br/site/aginov/servicos-tecnicos-especializados

- AGINOV — Página institucional: https://aginov.unemat.br/sobre
