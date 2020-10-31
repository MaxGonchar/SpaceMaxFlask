def get_header(token, header='Authorization', auth_type='Bearer'):
    return {f'{header}': f'{auth_type} {token}'}
