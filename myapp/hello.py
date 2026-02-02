import fire

def hello(name="Van"):
  return "Hello %s!" % name


if __name__ == '__main__':
  fire.Fire(hello)
