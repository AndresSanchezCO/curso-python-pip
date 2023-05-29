import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [1, 4, 2]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.savefig('pie_chart.png')
    plt.close()