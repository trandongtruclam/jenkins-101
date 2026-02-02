import fire

def hello(name="Jenkins"):
  return "Testing auto build of %s!" % name


if __name__ == '__main__':
  fire.Fire(hello)
