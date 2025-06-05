# chatbot_04.py
import customtkinter
from CTkMessagebox import CTkMessagebox
from datetime import datetime
import google.generativeai as genai

def abrir_chatbot():
    # Configura chave da API
    genai.configure(api_key='AIzaSyAgrmMrQktdBk06wtjd2CRgopGhXUI4rTc')

    # Carrega o modelo Gemini
    modelo = genai.GenerativeModel('gemini-2.0-flash-thinking-exp-1219')

    # Iniciar o histórico do chat
    chat = modelo.start_chat(history=[])

    # Função do chatbot
    def chatbot(mensagem):
        try:
            respostas = chat.send_message(mensagem)
            return f"{respostas.text}"
        except Exception as e:
            CTkMessagebox(title="Aviso- API", message=f"Ocorreu um erro ao obter a resposta - erro: {e}", icon="warning")

    # Função para processar a entrada do usuário
    def enviar_mensagem():
        mensagem_usuario = entrada_usuario.get()
        if mensagem_usuario.strip() == "":
            return
        
        resposta_chatbot = chatbot(mensagem_usuario)
        caixa_texto.insert(customtkinter.END, f"\n{label_id.cget('text')} {mensagem_usuario}\n", "usuario")
        caixa_texto.insert(customtkinter.END, f"Chatbot-AI: {resposta_chatbot}\n", "chatbot")
        entrada_usuario.delete(0, customtkinter.END)

    # Configuração da interface
    customtkinter.set_default_color_theme("dark-blue")
    customtkinter.set_appearance_mode("dark")

    # Criação da janela
    janela = customtkinter.CTk()
    janela.title("Bem-vindo ao Chatbot!")
    janela.geometry("420x560+500+50")
    janela.resizable(False, False)

    # Caixa de texto
    caixa_texto = customtkinter.CTkTextbox(janela, wrap=customtkinter.WORD, height=500, width=400)
    caixa_texto.pack()
    caixa_texto.tag_config("usuario", foreground="cyan", justify="left")
    caixa_texto.tag_config("chatbot", foreground="white")

    # Entrada do nome
    dialog = customtkinter.CTkInputDialog(text="Entre com seu nome:", title="Nome")
    nome = dialog.get_input()

    # Exibe mensagem inicial com data/hora
    data_hora = datetime.now()
    data_hora_text = data_hora.strftime("%d/%m/%Y %H:%M")
    caixa_texto.insert(customtkinter.END, f"[{data_hora_text}] \nChatbot-AI: Como posso te ajuda, {nome}?\n", "chatbot")

    # Frame inferior (entrada e botão)
    frame_0 = customtkinter.CTkFrame(janela)
    frame_0.pack(pady=10)

    # Rótulo com nome do usuário
    label_id = customtkinter.CTkLabel(frame_0, text=f"{nome}:", font=("Helvetica", 12, "bold"))
    label_id.grid(row=0, column=0, padx=5, pady=10)



    # Campo de entrada de texto
    entrada_usuario = customtkinter.CTkEntry(frame_0, width=200, font=("Helvetica", 12))
    entrada_usuario.grid(row=0, column=1, padx=5, pady=10)

    # Botão enviar
    botao_enviar = customtkinter.CTkButton(frame_0, text="Enviar", font=("Helvetica", 12, "bold"), command=enviar_mensagem)
    botao_enviar.grid(row=0, column=2, padx=5, pady=10)

    # Inicia o loop da interface do chatbot
    janela.mainloop()