# **Mastermind - INF1301**

## 📌 Descrição do Projeto
Este é um projeto desenvolvido como parte da disciplina **INF1301** e foi realizado em grupo. O jogo implementado é uma versão do **Mastermind**, um jogo de raciocínio lógico no qual o jogador precisa adivinhar uma senha oculta composta por uma sequência de cores.

O projeto segue o padrão de arquitetura **MVC (Model-View-Controller)** e foi desenvolvido utilizando **Python** com a biblioteca **Tkinter** para a interface gráfica.

---

## 🎮 Regras do Jogo
- O jogador deve adivinhar a senha oculta, que é uma sequência de cores.
- O jogo possui **três níveis de dificuldade** (1, 2 e 3), escalonando o desafio.
- O jogador pode selecionar cores e posicioná-las no tabuleiro para formar uma tentativa de combinação.
- O sistema fornece **feedback visual** sobre a tentativa:
  - ⚪ **Bola branca:** uma cor está correta, mas na posição errada.
  - ⚫ **Bola preta:** cor e posição estão corretas.
- O jogo possui um **número limitado de rodadas** para o jogador encontrar a solução.
- Mensagens são exibidas conforme o resultado:
  - 🎉 **"Parabéns, você ganhou!"** caso acerte a combinação dentro do limite de tentativas.
  - ❌ **"Você perdeu, tente de novo."** caso esgote as tentativas sem encontrar a senha correta.

---

## 🔥 Funcionalidades Adicionais
- 💾 **Salvamento e carregamento de partidas**: O programa permite salvar o progresso de uma partida e carregá-la posteriormente.

