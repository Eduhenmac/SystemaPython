Descrição do projeto:
Projeto de Python
Este projeto foi criado com o uso de banco de dados SQL Server da Microsoft
Para funcionar é preciso colocar o nome do servidor no arquivo banco como db_server e o nome do banco em db_database e icluir as seguites tabelas:

CREATE TABLE [dbo].[vendedor](
	[Numero_V] [int] IDENTITY(1,1) NOT NULL,
	[Nome] [varchar](50) NOT NULL,
	[Empresa] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Numero_V] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[produto](
	[Numero] [int] IDENTITY(1,1) NOT NULL,
	[Nome] [varchar](50) NOT NULL,
	[Empresa] [varchar](50) NOT NULL,
	[Preco] [float] NOT NULL,
	[Vendedor] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Numero] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[produto]  WITH CHECK ADD FOREIGN KEY([Vendedor])
REFERENCES [dbo].[vendedor] ([Numero_V])
GO