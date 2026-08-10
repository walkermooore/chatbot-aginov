# Sprint 1 — Fundamentação e Protocolo de Pesquisa

> **Projeto:** Chatbot informacional para apoio ao atendimento da AGINOV/UNEMAT  
> **Subprojeto:** Análise de requisitos, projeto e testes  
> **Sprint:** Sprint 1 — Fundamentação e protocolo de pesquisa  
> **Status:** Versão preliminar para validação com a orientadora e representantes autorizados da AGINOV  

## 1. Objetivo da Sprint

Consolidar as bases científicas, delimitar o escopo do protótipo, especificar os requisitos iniciais e definir como o artefato será avaliado.

A Sprint 1 tem como finalidade transformar a ideia geral do chatbot em um conjunto de decisões verificáveis, servindo como linha de base para as próximas sprints.

## 2. Entregas previstas

- Revisão bibliográfica inicial.
- Fichamentos e matriz de literatura.
- Requisitos funcionais, não funcionais e de conteúdo.
- Questões de avaliação e indicadores.
- Protocolo preliminar de coleta e análise.
- Análise de LGPD e necessidade de apreciação ética.
- Definição de pendências para validação com a AGINOV.

## 3. Declaração de escopo

O chatbot será um **protótipo web informacional**, voltado à triagem inicial de dúvidas relacionadas à AGINOV/UNEMAT.

O sistema deverá:

- responder perguntas frequentes;
- apresentar categorias de atendimento;
- encaminhar o usuário a canais oficiais;
- registrar perguntas não respondidas;
- utilizar fallback quando não houver resposta confiável;
- evitar coleta de dados pessoais desnecessários;
- informar que não substitui atendimento oficial.

O chatbot **não substituirá** análise técnica, jurídica ou administrativa realizada pela equipe da AGINOV.

## 4. Fundamentação inicial

A Sprint 1 foi organizada com base nos seguintes eixos:

| Eixo | Finalidade no projeto |
|---|---|
| Chatbots e PLN | Apoiar a compreensão de sistemas conversacionais e suas limitações. |
| Engenharia de Requisitos | Organizar identificação, documentação, validação e rastreabilidade dos requisitos. |
| Design Science Research | Justificar o desenvolvimento e avaliação do chatbot como artefato tecnológico. |
| Usabilidade e qualidade | Definir critérios para clareza, eficiência, satisfação e qualidade do produto. |
| LGPD e privacidade | Orientar minimização, transparência, segurança e responsabilidade no tratamento de dados. |

## 5. Escopo do MVP

O MVP deverá contemplar:

- protótipo web responsivo;
- atendimento informacional em português;
- perguntas digitadas e atalhos de perguntas frequentes;
- base de conhecimento estruturada;
- respostas com fonte oficial e data de revisão;
- fallback quando não houver resposta segura;
- encaminhamento para canais oficiais;
- registro mínimo de perguntas não respondidas;
- avaliação simples da utilidade da resposta;
- área administrativa restrita para manutenção da base;
- plano de testes funcional, fallback, qualidade das respostas, usabilidade, acessibilidade básica e privacidade.

## 6. Fora do escopo da primeira versão

Não fazem parte da primeira versão:

- protocolar pedidos de patente, marca, software ou desenho industrial;
- receber comunicado de invenção ou documentos técnicos;
- receber informações sigilosas pelo chatbot;
- realizar busca de anterioridade;
- emitir parecer técnico ou jurídico;
- acompanhar processos no INPI ou sistemas internos;
- tomar decisões administrativas;
- confirmar inscrições, prazos ou aprovações;
- substituir atendimento oficial;
- integrar com WhatsApp ou redes sociais;
- gerar respostas livres sem base validada;
- exigir cadastro de usuários externos;
- armazenar histórico integral das conversas.

## 7. Regras de negócio principais

| ID | Regra |
|---|---|
| RB01 | O chatbot terá finalidade exclusivamente informacional e deverá se identificar como assistente virtual. |
| RB02 | Toda resposta institucional deverá ser baseada em conteúdo aprovado ou fonte oficial cadastrada. |
| RB03 | O chatbot não poderá emitir parecer técnico ou jurídico, aceitar pedidos, aprovar documentos ou confirmar decisões administrativas. |
| RB05 | O sistema não solicitará dados pessoais desnecessários, documentos técnicos ou detalhes confidenciais de invenções. |
| RB07 | Informações sobre editais, eventos, prazos e inscrições deverão apresentar fonte oficial e data de atualização. |
| RB09 | Quando não houver resposta confiável, o sistema deverá utilizar fallback e indicar o próximo passo. |
| RB10 | Perguntas sem resposta poderão ser registradas apenas com os dados mínimos necessários. |
| RB13 | Cada resposta deverá manter fonte, versão, status, data de validação e data prevista para revisão. |
| RB14 | Conteúdo vencido, sem fonte ou reprovado não poderá ser usado em respostas públicas. |
| RB15 | Relatórios deverão priorizar indicadores agregados, evitando exposição de textos ou identificadores. |

## 8. Requisitos funcionais resumidos

| ID | Descrição | Prioridade |
|---|---|---|
| RF01 | Exibir saudação, identificação do assistente, finalidade informacional e aviso de que não substitui canais oficiais. | Must |
| RF02 | Permitir envio de perguntas em português por campo de texto. | Must |
| RF03 | Apresentar categorias e atalhos de perguntas frequentes. | Must |
| RF04 | Responder perguntas gerais sobre a AGINOV, sua atuação e seus públicos. | Should |
| RF05 | Orientar sobre propriedade intelectual e localizar formulários oficiais, sem receber arquivos. | Should |
| RF06 | Fornecer orientações iniciais sobre transferência de tecnologia, licenciamento, portfólio ou vitrine tecnológica. | Should |
| RF07 | Apresentar informações gerais sobre parcerias, PD&I, empreendedorismo, capacitações e ações de inovação. | Should |
| RF08 | Responder sobre editais, eventos e oportunidades somente com conteúdo vigente e validado. | Should |
| RF09 | Apresentar link ou identificação da fonte oficial e data de atualização nas respostas aplicáveis. | Must |
| RF10 | Utilizar apenas itens ativos e aprovados da base de conhecimento. | Must |
| RF11 | Executar fallback quando não houver resposta confiável. | Must |
| RF12 | Encaminhar ao atendimento humano perguntas administrativas, técnicas, jurídicas, confidenciais ou fora do escopo. | Must |
| RF13 | Registrar perguntas não respondidas de forma minimizada ou anonimizada. | Must |
| RF14 | Permitir avaliação simples da resposta, como “útil” ou “não útil”. | Must |
| RF15 | Alertar o usuário para não inserir dados pessoais, documentos, senhas ou informações confidenciais. | Must |
| RF16 | Identificar padrões básicos de conteúdo sensível e interromper armazenamento quando necessário. | Should |
| RF17 | Disponibilizar autenticação para usuários administrativos. | Must |
| RF18 | Permitir cadastro, edição, visualização e desativação de perguntas, variações e respostas. | Must |
| RF19 | Organizar conteúdos por categoria, palavras-chave ou intenção. | Must |
| RF20 | Registrar fonte, status, responsável, data de validação e data de revisão. | Must |
| RF21 | Registrar histórico de alterações relevantes na base. | Should |
| RF22 | Consultar indicadores agregados de perguntas sem resposta, fallback e avaliações. | Should |
| RF23 | Permitir cadastro de bateria de perguntas e respostas esperadas para testes. | Should |
| RF24 | Exportar resultados de testes e indicadores em formato simples. | Could |

> Os requisitos RF04 a RF08 dependem da existência de conteúdo institucional validado. Caso o conteúdo ainda não esteja validado, o chatbot deverá acionar fallback ou encaminhar o usuário aos canais oficiais.

## 9. Requisitos não funcionais resumidos

| ID | Atributo | Prioridade |
|---|---|---|
| RNF01 | Correção das respostas previstas na bateria principal. | Must |
| RNF02 | Rastreabilidade das respostas institucionais. | Must |
| RNF03 | Atualidade de conteúdos com prazo, evento, contato ou edital. | Must |
| RNF04 | Clareza das respostas em português brasileiro. | Must |
| RNF05 | Consistência entre perguntas semanticamente equivalentes. | Must |
| RNF06 | Usabilidade em tarefas principais do teste exploratório. | Should |
| RNF07 | Registro de satisfação, preferencialmente com SUS. | Should |
| RNF08 | Acessibilidade básica da interface. | Must |
| RNF09 | Responsividade em computador e celular. | Must |
| RNF10 | Tempo de resposta adequado em ambiente de teste. | Should |
| RNF12 | Uso de HTTPS em implantação acessível pela internet. | Must |
| RNF13 | Controle de acesso administrativo. | Must |
| RNF14 | Armazenamento seguro de credenciais. | Must |
| RNF15 | Minimização de dados pessoais. | Must |
| RNF16 | Definição de prazo de retenção e exclusão/agregação. | Must |
| RNF17 | Uso de dados agregados em relatórios. | Must |
| RNF18 | Proteção contra envio e armazenamento de informações sigilosas. | Must |
| RNF19 | Atualização de conteúdos sem alteração direta no código-fonte. | Must |
| RNF20 | Arquitetura compatível com backend em Python/Django e interface web integrada. | Must |
| RNF21 | PostgreSQL planejado para implantação; SQLite apenas para desenvolvimento e testes iniciais. | Should |
| RNF23 | Cada requisito Must deverá possuir caso de teste rastreável. | Must |
| RNF24 | Registro de alterações administrativas relevantes. | Should |
| RNF25 | Procedimento simples de backup e restauração. | Should |
| RNF26 | Instruções de instalação, dependências e variáveis de ambiente sem expor segredos. | Should |

## 10. Requisitos de conteúdo da base de conhecimento

| ID | Requisito de conteúdo | Prioridade |
|---|---|---|
| RC01 | Informações gerais sobre a AGINOV, atuação, públicos atendidos e canais institucionais. | Must |
| RC02 | Orientações iniciais sobre propriedade intelectual, sem parecer técnico ou jurídico. | Must |
| RC03 | Orientação sobre comunicado de invenção e formulários oficiais, sem receber documentos pelo chatbot. | Must |
| RC04 | Informações iniciais sobre transferência de tecnologia, licenciamento, portfólio ou vitrine tecnológica, quando houver fonte oficial validada. | Should |
| RC05 | Informações sobre parcerias, PD&I, empreendedorismo, capacitações e ações de inovação. | Should |
| RC06 | Informações sobre editais, eventos e oportunidades somente com conteúdo vigente, fonte oficial e data de atualização. | Should |
| RC07 | Canais oficiais de contato e atendimento humano para situações fora do escopo ou que exigem análise. | Must |
| RC08 | Registro de categoria, criticidade, fonte, link, status, responsável, validação, revisão e versão para cada conteúdo. | Must |

## 11. Estrutura mínima da base de conhecimento

Cada item da base deverá possuir:

- código;
- categoria;
- pergunta principal;
- variações;
- palavras-chave ou intenção;
- resposta aprovada;
- fonte oficial;
- link oficial, quando aplicável;
- criticidade;
- status;
- responsável pela validação;
- data da validação;
- próxima revisão;
- versão.

## 12. Classificação de criticidade

| Nível | Tratamento |
|---|---|
| Crítica | Prazos, editais, procedimentos de proteção, documentos, decisões ou informações cuja incorreção possa causar prejuízo. |
| Alta | Orientações sobre propriedade intelectual, transferência de tecnologia, parcerias, contatos institucionais e procedimentos que possam exigir análise da equipe da AGINOV. |
| Média | Descrição de serviços, categorias de atendimento, explicações gerais e orientações institucionais de baixo risco. |
| Baixa | Saudações, ajuda de navegação e mensagens de apresentação do assistente. |

Conteúdos críticos ou de alta criticidade não deverão ser apresentados sem fonte oficial, status aprovado e data de revisão válida.

## 13. LGPD e privacidade

O protótipo deverá aplicar minimização de dados e privacidade por concepção.

Diretrizes principais:

- o uso público não exigirá cadastro;
- não solicitar CPF, matrícula, telefone, endereço ou e-mail;
- evitar armazenamento integral de perguntas digitadas;
- registrar feedback de forma anônima ou agregada;
- não registrar IP no banco da pesquisa, salvo necessidade técnica justificada;
- restringir acesso a contas administrativas;
- definir política de retenção antes da implantação pública;
- excluir, anonimizar ou agregar dados após a finalidade.

## 14. Questões de avaliação

| ID | Questão |
|---|---|
| QA1 | O chatbot cobre as principais categorias e dúvidas informacionais priorizadas pela AGINOV? |
| QA2 | As respostas são corretas, claras, atuais e rastreáveis a fontes oficiais? |
| QA3 | Os usuários conseguem formular perguntas e localizar orientações com eficácia e eficiência? |
| QA4 | O sistema reconhece adequadamente perguntas desconhecidas, ambíguas, confidenciais ou fora do escopo? |
| QA5 | O encaminhamento para atendimento humano ocorre nas situações apropriadas? |
| QA6 | A coleta e o armazenamento de dados permanecem limitados ao necessário? |
| QA7 | A base de conhecimento pode ser mantida e auditada pela equipe autorizada sem alteração do código? |

## 15. Indicadores

| ID | Indicador | Fonte |
|---|---|---|
| I01 | Cobertura da base | Bateria de perguntas |
| I02 | Adequação das respostas | Rubrica de especialistas |
| I03 | Erros críticos | Relatório de testes |
| I04 | Rastreabilidade | Base e testes |
| I05 | Conclusão de tarefas | Teste de usabilidade |
| I06 | Tempo de tarefa | Observação |
| I07 | Satisfação percebida | Questionário |
| I08 | Fallback adequado | Teste de fallback |
| I09 | Encaminhamento adequado | Teste funcional |
| I10 | Minimização de dados | Revisão de privacidade |
| I11 | Perguntas não respondidas | Logs minimizados |
| I12 | Manutenção da base | Teste administrativo |

## 16. Critérios de aceite da Sprint 1

| ID | Critério | Situação |
|---|---|---|
| CA01 | Referências iniciais organizadas por eixo temático. | Atendido; manter atualização da matriz. |
| CA02 | Fichamentos e matriz de literatura disponíveis. | Atendido nas seções de síntese e matriz de literatura. |
| CA03 | Escopo do MVP e itens fora do escopo registrados. | Atendido na seção de escopo. |
| CA04 | Regras institucionais convertidas em regras de negócio. | Atendido; requer validação da AGINOV. |
| CA05 | Requisitos funcionais, não funcionais e de conteúdo identificados, priorizados e verificáveis. | Atendido nas seções 9, 10 e 11. |
| CA06 | Cada indicador relacionado a uma questão e a uma fonte de dados. | Atendido na seção de avaliação. |
| CA07 | Protocolo preliminar evita coleta desnecessária de dados pessoais. | Atendido nas seções de dados, coleta e LGPD. |
| CA08 | Necessidade de apreciação ética analisada antes da coleta com pessoas. | Atendido na seção de ética. |
| CA09 | Documento apresentado à orientadora e equipe autorizada para validação. | Pendente de reunião de validação. |
| CA10 | Alterações solicitadas registradas em nova versão. | Pendente após validação. |

## 17. Pendências para encerramento formal

- Confirmar com a AGINOV as categorias, fontes, contatos e conteúdos prioritários.
- Designar funções responsáveis pela validação e revisão da base de conhecimento.
- Aprovar ou ajustar os requisitos Must e suas metas preliminares.
- Definir política de retenção de perguntas não respondidas e logs.
- Consultar orientação institucional sobre ética antes de entrevistas ou testes com participantes.
- Registrar ata ou formulário de validação.
- Emitir a versão 1.1 do documento após validação.

## 18. Próxima etapa

A próxima sprint deverá transformar os requisitos aprovados em:

- histórias de usuário;
- fluxos conversacionais;
- protótipos de tela;
- casos de teste;
- estrutura inicial da base de conhecimento;
- backlog técnico de implementação.

## 19. Observação

Este arquivo resume a documentação da Sprint 1 para uso no GitHub. O documento completo deve permanecer arquivado em PDF na pasta de documentação do projeto.
