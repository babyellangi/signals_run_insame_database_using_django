 Django signals run in the same database transaction as the caller. This means that any database operations performed in a signal receiver will be part of the same transaction initiated by the signal emitter.
