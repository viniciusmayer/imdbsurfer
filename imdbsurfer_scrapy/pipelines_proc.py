import pika, sys, os, psycopg2, configparser

selectSetMovieIndex = 'select set_movie_index();'


def get_connection():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    host = config['DATABASE']['host']
    schema = config['DATABASE']['schema']
    user = config['DATABASE']['user']
    passw = config['DATABASE']['pass']
    return 'dbname={0} user={1} host={2} password={3}'.format(schema, user, host, passw)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    connection = psycopg2.connect(get_connection())
    cursor = connection.cursor()
    cursor.execute(selectSetMovieIndex)
    connection.commit()


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='imdbsurferq')
    channel.basic_consume(queue='imdbsurferq', auto_ack=True, on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)