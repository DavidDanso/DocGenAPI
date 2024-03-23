from pyhanko import stamp
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields, signers
from pyhanko.keys import load_cert_from_pemder
from pyhanko_certvalidator import ValidationContext
from .config import app_settings

def sign_pdf(document_path, position, stamp_text='THIS IS A SIGNED DOCUMENT!\nSigned by: %(signer)s\nTime: %(ts)s'):
    # Load the signer's certificate and private key
    # replace with path to test_pfx.pfx file
    cms_signer = signers.SimpleSigner.load_pkcs12(pfx_file=app_settings.PFX_FILE, passphrase=app_settings.PASSPHRASE.encode('utf-8'))

    # Load the root certificate for validation
    # replace with path to cert.pem file
    root_cert = load_cert_from_pemder(app_settings.CERT_PEM_FILE)
    vc = ValidationContext(trust_roots=[root_cert])

    # Read the existing PDF document
    with open(document_path, 'rb') as doc:
        # Create an IncrementalPdfFileWriter
        w = IncrementalPdfFileWriter(doc)

        # Append a signature field to the PDF
        fields.append_signature_field(w, sig_field_spec=fields.SigFieldSpec('Signature', box=position))

        # Configure the PDF signer
        meta = signers.PdfSignatureMetadata(field_name='Signature')
        pdf_signer = signers.PdfSigner(
            meta,
            signer=cms_signer,
            stamp_style=stamp.TextStampStyle(stamp_text=stamp_text)
        )

        # Sign the PDF and save the signed document
        signed_doc_path = 'signed-document.pdf'
        with open(signed_doc_path, 'wb') as outf:
            pdf_signer.sign_pdf(w, output=outf)

    return f'Document signed successfully!'


