import streamlit as st
from banco import add_pedido, add_feedback, inicializar_banco



# Configuração do estilo da página
st.set_page_config(page_title="Cookies da Renata", page_icon="🍪", layout="wide")

# Título principal e subtítulo
st.title("🍪Bem-vindo ao Cookies da Renata!🍪")
st.subheader("**Clique na seta ao lado para selecionar seus Cookies!**")
st.subheader("Faça seu pedido de cookies e deixe seu feedback.")

# Barra lateral com o menu de cookies
st.sidebar.header("🍪 Menu de Cookies")

# Opções de cookies disponíveis
cookies = {
    "NUTELLA": 13.00,
    "RED VELVET": 13.00,
    "CHOCO NINHO": 13.00,
    "CHOCOLATE CHIP": 13.00,
    "LIMAO": 13.00,
    "FRUTAS VERMELHAS": 14.00,
    "M&M": 13.00,
    "PRESTIGIO": 13.00,
    "PAÇOCA": 13.00,
    "OVOMALTINE": 14.00
}

# Seleção de cookies na barra lateral
selected_cookies = []
for cookie, price in cookies.items():
    quantity = st.sidebar.number_input(f"{cookie} ($ {price:.2f} cada)", min_value=0, max_value=20, step=1)
    if quantity > 0:
        selected_cookies.append((cookie, quantity, price))

# Exibir os cookies selecionados
if selected_cookies:
    st.header("Seu Pedido de Cookies")
    total = 0
    for cookie, quantity, price in selected_cookies:
        st.write(f"{quantity}x {cookie} - $ {quantity * price:.2f}")
        total += quantity * price

    st.write(f"**Total: $ {total:.2f}**")

    # Formulário para inserir nome do cliente e WhatsApp
    cliente = st.text_input("Nome do Cliente", max_chars=100)
    whatsapp = st.text_input("WhatsApp do Cliente", max_chars=20)

    # Botão de confirmação do pedido
    if st.button("Confirmar Pedido", key="confirmar_pedido"):
        if cliente and whatsapp:
            pedido_info = ""
            for cookie, quantity, price in selected_cookies:
                add_pedido(cookie, quantity, price, cliente, whatsapp)
                pedido_info += f"{quantity}x {cookie}, "
            pedido_info = pedido_info[:-2]  # Remover a última vírgula e espaço

            # Gera o link "Click to Chat" do WhatsApp
            mensagem = f"Pedido confirmado para {cliente}. Itens: {pedido_info}. Total: ${total:.2f}."
            link_whatsapp = f"https://wa.me/5562986039187?text={mensagem.replace(' ', '%20')}"

            # Exibe o link no Streamlit
            st.markdown(f"[Clique aqui para enviar a confirmação pelo WhatsApp]({link_whatsapp})")
            st.success("Pedido confirmado com sucesso! Clique no link acima para enviar a mensagem pelo WhatsApp.")
            st.balloons()
        else:
            st.error("O nome e o WhatsApp do cliente não podem ser nulos. Por favor, preencha ambos.")
else:
    st.write("Nenhum cookie selecionado ainda.")

# Seção de feedback
st.header("Deixe seu Feedback")
name = st.text_input("Seu Nome")
feedback = st.text_area("Seu Feedback")

# Botão de envio de feedback
if st.button("Enviar Feedback", key="enviar_feedback"):
    if name and feedback:
        add_feedback(name, feedback)
        st.success("Obrigado pelo seu feedback!")
    else:
        st.error("Por favor, preencha seu nome e seu feedback antes de enviar.")

# Footer personalizado
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0A0001;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: white;
    }
    </style>
    <div class="footer">
        Desenvolvido por Thiago Henrique. © 2024 Todos os direitos reservados.
    </div>
    """, unsafe_allow_html=True
)
st.markdown(
    """
    <style>
        /* Se o ícone do GitHub é um link com uma classe específica */
        .github-icon {
            display: none;
        }
        
        /* Se o ícone do GitHub é um link específico */
        a[href*="github.com"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)
