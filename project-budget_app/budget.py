OUTPUT_SIZE = 30
DESCRIPTION_WIDTH = 23
AMOUNT_WIDTH = 7


class Category:

  def __init__(self, category: str) -> None:
    self.name = category
    self.ledger = []

  def get_name(self) -> str:
    return self.name

  def deposit(self, amount: float, description: str = '') -> None:
    self.ledger.append(dict(amount=amount, description=description))

  def withdraw(self, amount: float, description: str = '') -> bool:
    if self.check_funds(amount):
      self.ledger.append(dict(amount=-1 * amount, description=description))
      return True
    else:
      return False

  def get_balance(self) -> float:
    balance = 0
    for i in range(len(self.ledger)):
      balance += self.ledger[i]['amount']
    return balance

  def transfer(self, amount: float, category: object) -> bool:
    if self.check_funds(amount):
      self.withdraw(amount, description=f'Transfer to {category.get_name()}')
      category.deposit(amount, description=f'Transfer from {self.name}')
      return True
    else:
      return False

  def check_funds(self, amount: float) -> bool:
    return self.get_balance() >= amount

  def __str__(self) -> str:
    title_diff = 0
    output = ''
    total = 0
    if len(self.name) % 2 == 1:
      title_diff = 1
    asterisk_count = int((OUTPUT_SIZE - len(self.name)) / 2)
    output += '*' * asterisk_count + self.name + '*' * (asterisk_count +
                                                        title_diff) + '\n'
    for i in range(len(self.ledger)):
      output += (self.ledger[i]['description'][:DESCRIPTION_WIDTH] +
                 ' ' * 23)[:23]
      output += (' ' * 7 + str("{:.2f}".format(self.ledger[i]['amount'])))[-1 * AMOUNT_WIDTH:]
      output += '\n'
      total += self.ledger[i]['amount']
    output += 'Total: ' + str(total)
    return output

  def get_spend(self) -> float:
    spend = 0
    for i in range(len(self.ledger)):
      if self.ledger[i]['amount'] < 0:
        spend += self.ledger[i]['amount']
    return spend


def create_spend_chart(categories: list):
  cat_names = []
  cat_spend = []
  cat_pct = []
  chart_output = ''
  total_spend = 0
  max_len_cat = 0
  x_len = len(categories) * 3 + 1
  for i in range(len(categories)):    
    cat_names.append(categories[i].get_name())
    cat_spend.append(categories[i].get_spend())
    total_spend += cat_spend[i]
  for i in range(len(cat_names)):
    if (len(cat_names[i]) > max_len_cat):
      max_len_cat = len(cat_names[i])
    cat_pct.append(int(cat_spend[i] / total_spend / .1) * .1)

  chart_output += 'Percentage spent by category\n'
  for i in reversed(range(11)):
    chart_output += f"{('  '+str(i*10))[-3:]}|"
    for j in range(len(cat_pct)):
      chart_output += f" {'o' if cat_pct[j] >= i*.1 else ' '} "
    chart_output += ' \n'
  chart_output += '    '+('-'*x_len)+'\n'
  for i in range(max_len_cat):
    chart_output += '    '
    for j in range(len(cat_names)):
      if len(cat_names[j]) <= i:
        chart_output += '   '
      else:
        chart_output += f' {cat_names[j][i]} '
    chart_output += ' \n' if i < max_len_cat-1 else ' '
  return chart_output