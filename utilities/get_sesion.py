import tls_client

def get_session():
    session = tls_client.Session(
        client_identifier="chrome_120",
        random_tls_extension_order=True,
        ja3_string="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,10-23-27-43-13-65281-16-5-45-18-0-11-35-17513-51-21-41,29-23-24,0",
        h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},
        h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],
        supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],
        supported_versions=["GREASE", "1.3", "1.2"],
        key_share_curves=["GREASE", "X25519"],
        cert_compression_algo="brotli",
        connection_flow=15663105,
    )
    return session